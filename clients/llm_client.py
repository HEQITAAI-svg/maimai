"""LLM 客户端 - 支持 OpenAI 兼容格式的聚合平台"""

from __future__ import annotations

import json
import logging
import sys
import threading
import time

import httpx
from openai import OpenAI

logger = logging.getLogger(__name__)


def _spinner(stop_event: threading.Event):
    """后台旋转动画，让用户知道还在等待"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    i = 0
    start = time.time()
    while not stop_event.is_set():
        elapsed = int(time.time() - start)
        sys.stderr.write(f"\r  {chars[i % len(chars)]} 等待 LLM 响应... {elapsed}s")
        sys.stderr.flush()
        i += 1
        stop_event.wait(0.2)
    sys.stderr.write("\r" + " " * 40 + "\r")
    sys.stderr.flush()


class LLMClient:
    """统一的 LLM 客户端，通过 base_url 适配任意 OpenAI 兼容平台"""

    def __init__(self, base_url: str, api_key: str, model: str, timeout: int = 300):
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=httpx.Timeout(timeout, connect=15),
        )
        self.model = model

    def chat(self, messages: list[dict], temperature: float = 0.7, max_tokens: int = 4096) -> str:
        """发送聊天请求，返回文本内容（带等待动画）"""
        logger.info(f"调用 LLM: model={self.model}")

        # 启动等待动画
        stop = threading.Event()
        spinner = threading.Thread(target=_spinner, args=(stop,), daemon=True)
        spinner.start()

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        finally:
            stop.set()
            spinner.join()

        content = response.choices[0].message.content
        if not content:
            logger.error(f"LLM 返回空内容, finish_reason={response.choices[0].finish_reason}")
            raise ValueError("LLM 返回了空内容，请检查 API Key 和模型名称是否正确")

        logger.info(f"LLM 返回 {len(content)} 字符")
        return content

    def chat_json(self, messages: list[dict], temperature: float = 0.7, max_tokens: int = 4096) -> dict:
        """发送聊天请求，解析 JSON 返回"""
        content = self.chat(messages, temperature=temperature, max_tokens=max_tokens)

        # 尝试从回复中提取 JSON
        content = content.strip()
        if content.startswith("```"):
            lines = content.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            content = "\n".join(lines)

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.warning("LLM 返回内容不是有效 JSON，尝试提取...")
            start = content.find("{")
            end = content.rfind("}") + 1
            if start != -1 and end > start:
                return json.loads(content[start:end])
            raise ValueError(f"无法从 LLM 回复中解析 JSON:\n{content[:500]}")
