"""阶段4：渲染 Markdown 学习路径文档"""

from __future__ import annotations

import logging
import os
import re
from datetime import datetime

from models.schema import PipelineContext, Resource
from pipeline.base import PipelineStage

logger = logging.getLogger(__name__)

LEVEL_ICONS = {
    "入门": "🟢",
    "进阶": "🟡",
    "高级": "🔴",
    "实战": "🚀",
}

RESOURCE_ICONS = {
    "video": "📺",
    "article": "📄",
    "github": "💻",
}

RESOURCE_LABELS = {
    "video": "视频",
    "article": "文章",
    "github": "GitHub 项目",
}


class MarkdownRenderer(PipelineStage):
    """将学习框架和资源渲染为 Markdown 文件"""

    def __init__(self, output_dir: str = "./output"):
        self.output_dir = output_dir

    def process(self, context: PipelineContext) -> PipelineContext:
        if not context.framework:
            raise ValueError("缺少学习框架，无法渲染")

        fw = context.framework
        lines: list[str] = []

        # 标题
        lines.append(f"# {fw.topic} - 学习路径\n")
        lines.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

        # 总览
        lines.append("## 📖 学习概览\n")
        lines.append(f"{fw.overview}\n")

        # 路径总览
        lines.append("## 🗺️ 路径总览\n")
        lines.append("| 阶段 | 主题 | 知识点数 |")
        lines.append("|------|------|---------|")
        for stage in fw.stages:
            icon = LEVEL_ICONS.get(stage.level, "📌")
            lines.append(f"| {icon} {stage.level} | {stage.title} | {len(stage.points)} |")
        lines.append("")

        # 各阶段详情
        for stage_idx, stage in enumerate(fw.stages, 1):
            icon = LEVEL_ICONS.get(stage.level, "📌")
            lines.append(f"## {icon} 阶段{stage_idx}：{stage.level} - {stage.title}\n")

            if stage.description:
                lines.append(f"{stage.description}\n")

            for point_idx, point in enumerate(stage.points, 1):
                lines.append(f"### {stage_idx}.{point_idx} {point.title}\n")

                if point.summary:
                    lines.append(f"{point.summary}\n")

                # 关联资源
                resources = context.resources.get(point.title, [])
                if resources:
                    lines.append("**推荐资源：**\n")

                    # 按类型分组
                    for rtype in ["video", "article", "github"]:
                        typed = [r for r in resources if r.type == rtype]
                        if typed:
                            icon_r = RESOURCE_ICONS.get(rtype, "🔗")
                            label = RESOURCE_LABELS.get(rtype, rtype)
                            lines.append(f"**{icon_r} {label}：**\n")
                            for r in typed:
                                desc = f" - {r.description}" if r.description else ""
                                lines.append(f"- [{r.title}]({r.url}){desc}")
                            lines.append("")

            lines.append("---\n")

        # 尾部
        lines.append("> 本学习路径由 AI 自动生成，资源链接来自互联网搜索，请注意甄别内容质量。\n")

        markdown = "\n".join(lines)
        context.markdown = markdown

        # 保存文件
        os.makedirs(self.output_dir, exist_ok=True)
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', fw.topic)
        filepath = os.path.join(self.output_dir, f"{safe_name}_学习路径.md")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        logger.info(f"Markdown 文件已保存: {filepath}")
        return context
