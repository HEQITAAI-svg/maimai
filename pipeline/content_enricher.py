"""阶段3：LLM 对搜索结果进行二次加工和筛选"""

from __future__ import annotations

import json
import logging

from clients.llm_client import LLMClient
from models.schema import PipelineContext, Resource
from pipeline.base import PipelineStage

logger = logging.getLogger(__name__)

ENRICH_PROMPT = """你是一位技术学习顾问。下面是关于「{point_title}」这个知识点搜索到的学习资源列表。

请帮我：
1. 从中筛选出最优质、最相关的资源（每类保留最多3条）
2. 为每条资源写一句简短的推荐理由

资源列表：
{resources_json}

请严格按以下 JSON 格式输出：
{{
  "filtered": [
    {{
      "title": "资源标题",
      "url": "资源链接",
      "type": "video/article/github",
      "description": "推荐理由（一句话）"
    }}
  ]
}}"""


class ContentEnricher(PipelineStage):
    """使用 LLM 对搜索结果进行质量筛选和摘要增强"""

    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def process(self, context: PipelineContext) -> PipelineContext:
        if not context.resources:
            logger.warning("没有资源需要筛选，跳过内容增强阶段")
            context.enriched = True
            return context

        total = len(context.resources)
        enriched_resources: dict[str, list[Resource]] = {}

        for i, (point_title, resources) in enumerate(context.resources.items(), 1):
            logger.info(f"[{i}/{total}] 筛选资源: {point_title}")

            if not resources:
                enriched_resources[point_title] = []
                continue

            # 如果资源较少，不需要 LLM 筛选
            if len(resources) <= 6:
                enriched_resources[point_title] = resources
                continue

            resources_data = [
                {"title": r.title, "url": r.url, "type": r.type, "description": r.description}
                for r in resources
            ]

            prompt = ENRICH_PROMPT.format(
                point_title=point_title,
                resources_json=json.dumps(resources_data, ensure_ascii=False, indent=2),
            )

            try:
                result = self.llm.chat_json(
                    [{"role": "user", "content": prompt}],
                    temperature=0.3,
                )
                filtered = result.get("filtered", [])
                enriched_resources[point_title] = [
                    Resource(**item) for item in filtered
                ]
            except Exception as e:
                logger.warning(f"筛选 [{point_title}] 资源失败: {e}，保留原始结果")
                enriched_resources[point_title] = resources[:9]  # 每类保留3条

        context.resources = enriched_resources
        context.enriched = True
        logger.info("内容增强完毕")
        return context
