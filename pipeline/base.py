"""Pipeline 基类与编排引擎"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from models.schema import PipelineContext

logger = logging.getLogger(__name__)


class PipelineStage(ABC):
    """Pipeline 阶段基类"""

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def process(self, context: PipelineContext) -> PipelineContext:
        """处理上下文并返回更新后的上下文"""
        ...


class Pipeline:
    """Pipeline 编排引擎，按顺序执行各阶段"""

    def __init__(self, stages: list[PipelineStage]):
        self.stages = stages

    def run(self, topic: str) -> PipelineContext:
        context = PipelineContext(topic=topic)
        total = len(self.stages)

        for i, stage in enumerate(self.stages, 1):
            logger.info(f"[{i}/{total}] 执行阶段: {stage.name}")
            try:
                context = stage.process(context)
            except Exception as e:
                logger.error(f"阶段 {stage.name} 执行失败: {e}")
                raise

        return context
