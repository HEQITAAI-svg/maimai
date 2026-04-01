"""数据模型定义"""

from __future__ import annotations

from pydantic import BaseModel, Field


class KnowledgePoint(BaseModel):
    """单个知识点"""
    title: str
    summary: str = ""
    search_keywords: list[str] = Field(default_factory=list)


class LearningStage(BaseModel):
    """学习阶段（入门/进阶/高级/实战）"""
    level: str
    title: str
    description: str = ""
    points: list[KnowledgePoint] = Field(default_factory=list)


class Resource(BaseModel):
    """学习资源（视频/文章/GitHub项目）"""
    title: str
    url: str
    type: str  # "video" | "article" | "github"
    description: str = ""


class LearningFramework(BaseModel):
    """完整的学习框架"""
    topic: str
    overview: str = ""
    stages: list[LearningStage] = Field(default_factory=list)


class PipelineContext(BaseModel):
    """Pipeline 上下文，在各阶段间传递"""
    topic: str
    framework: LearningFramework | None = None
    resources: dict[str, list[Resource]] = Field(default_factory=dict)
    enriched: bool = False
    markdown: str = ""
