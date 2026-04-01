"""阶段2：搜索引擎获取真实资源链接"""

from __future__ import annotations

import logging

from clients.search_client import SearchClient
from models.schema import PipelineContext
from pipeline.base import PipelineStage

logger = logging.getLogger(__name__)


class ResourceSearcher(PipelineStage):
    """为每个知识点搜索视频、文章、GitHub 项目"""

    def __init__(self, search_client: SearchClient):
        self.searcher = search_client

    def process(self, context: PipelineContext) -> PipelineContext:
        if not context.framework:
            raise ValueError("缺少学习框架，请先运行 FrameworkGenerator")

        total_points = sum(len(s.points) for s in context.framework.stages)
        current = 0

        for stage in context.framework.stages:
            for point in stage.points:
                current += 1
                keywords = " ".join(point.search_keywords) if point.search_keywords else point.title
                logger.info(
                    f"[{current}/{total_points}] 搜索资源: {point.title} "
                    f"(关键词: {keywords})"
                )

                resources = self.searcher.search_all(keywords)
                # 用知识点标题作为 key 关联资源
                context.resources[point.title] = resources

                logger.info(
                    f"  找到 {len(resources)} 条资源 "
                    f"(文章: {sum(1 for r in resources if r.type == 'article')}, "
                    f"视频: {sum(1 for r in resources if r.type == 'video')}, "
                    f"GitHub: {sum(1 for r in resources if r.type == 'github')})"
                )

        logger.info(f"资源搜索完毕，共收集 {sum(len(v) for v in context.resources.values())} 条资源")
        return context
