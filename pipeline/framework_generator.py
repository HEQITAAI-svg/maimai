"""阶段1：LLM 生成学习框架"""

from __future__ import annotations

import logging

from clients.llm_client import LLMClient
from models.schema import (
    KnowledgePoint,
    LearningFramework,
    LearningStage,
    PipelineContext,
)
from pipeline.base import PipelineStage

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """你是一位资深的技术教育专家，擅长为任何技术领域设计由浅入深的学习路径。

请根据用户给出的学习主题，生成一个结构化的学习框架。要求：
1. 分为 4 个阶段：入门、进阶、高级、实战
2. 每个阶段包含 3-5 个核心知识点
3. 每个知识点附带简要说明和用于搜索资源的英文关键词
4. 内容由浅入深，循序渐进

严格按以下 JSON 格式输出，不要输出其他内容：
{
  "topic": "主题名称",
  "overview": "这个领域的总体介绍（200字左右）",
  "stages": [
    {
      "level": "入门",
      "title": "阶段标题",
      "description": "阶段描述",
      "points": [
        {
          "title": "知识点标题",
          "summary": "知识点摘要（100字左右）",
          "search_keywords": ["keyword1", "keyword2"]
        }
      ]
    }
  ]
}"""


class FrameworkGenerator(PipelineStage):
    """调用 LLM 生成结构化学习框架"""

    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def process(self, context: PipelineContext) -> PipelineContext:
        logger.info(f"正在为 [{context.topic}] 生成学习框架...")

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"请为以下主题生成学习路径：{context.topic}"},
        ]

        data = self.llm.chat_json(messages, temperature=0.7)

        framework = LearningFramework(
            topic=data.get("topic", context.topic),
            overview=data.get("overview", ""),
            stages=[
                LearningStage(
                    level=s["level"],
                    title=s["title"],
                    description=s.get("description", ""),
                    points=[
                        KnowledgePoint(
                            title=p["title"],
                            summary=p.get("summary", ""),
                            search_keywords=p.get("search_keywords", []),
                        )
                        for p in s.get("points", [])
                    ],
                )
                for s in data.get("stages", [])
            ],
        )

        logger.info(
            f"学习框架生成完毕: {len(framework.stages)} 个阶段, "
            f"共 {sum(len(s.points) for s in framework.stages)} 个知识点"
        )

        context.framework = framework
        return context
