"""知识学习路径生成器 - CLI 入口"""

from __future__ import annotations

import argparse
import logging
import os
import sys

import yaml
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel

from clients.llm_client import LLMClient
from clients.search_client import SearchClient
from pipeline import (
    ContentEnricher,
    FrameworkGenerator,
    MarkdownRenderer,
    Pipeline,
    ResourceSearcher,
)


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置文件"""
    if not os.path.exists(config_path):
        print(f"配置文件不存在: {config_path}")
        print("请复制 config.yaml 并填入你的 API Key")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(rich_tracebacks=True, show_time=False)],
    )


def main():
    parser = argparse.ArgumentParser(
        description="知识学习路径生成器 - 输入一个领域，生成由浅入深的学习路径",
    )
    parser.add_argument("topic", nargs="?", help="学习主题，例如：多智能体编排")
    parser.add_argument("-c", "--config", default="config.yaml", help="配置文件路径")
    parser.add_argument("-o", "--output", help="输出目录（覆盖配置文件中的设置）")
    parser.add_argument("--no-enrich", action="store_true", help="跳过内容增强阶段（节省 API 调用）")

    args = parser.parse_args()

    setup_logging()
    console = Console()

    # 交互式输入
    topic = args.topic
    if not topic:
        topic = console.input("[bold green]请输入你想学习的主题：[/] ").strip()
        if not topic:
            console.print("[red]主题不能为空[/]")
            sys.exit(1)

    # 加载配置
    config = load_config(args.config)
    llm_config = config.get("llm", {})
    search_config = config.get("search", {})
    output_config = config.get("output", {})

    # 检查 API Key
    api_key = llm_config.get("api_key", "") or os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        console.print("[red]请在 config.yaml 中配置 llm.api_key 或设置环境变量 OPENAI_API_KEY[/]")
        sys.exit(1)

    # 初始化客户端
    llm_client = LLMClient(
        base_url=llm_config.get("base_url", "https://api.openai.com/v1"),
        api_key=api_key,
        model=llm_config.get("model", "gpt-4o"),
        timeout=llm_config.get("timeout", 120),
    )

    search_client = SearchClient(
        max_results=search_config.get("max_results_per_type", 5),
        github_token=search_config.get("github_token", "") or os.environ.get("GITHUB_TOKEN", ""),
    )

    output_dir = args.output or output_config.get("dir", "./output")

    # 构建 Pipeline
    stages = [
        FrameworkGenerator(llm_client),
        ResourceSearcher(search_client),
    ]
    if not args.no_enrich:
        stages.append(ContentEnricher(llm_client))
    stages.append(MarkdownRenderer(output_dir))

    pipeline = Pipeline(stages)

    # 运行
    console.print(Panel(
        f"[bold]主题：[cyan]{topic}[/cyan]\n"
        f"模型：{llm_config.get('model', 'gpt-4o')}\n"
        f"阶段：{len(stages)} 个\n"
        f"输出：{output_dir}/",
        title="🎓 知识学习路径生成器",
        border_style="green",
    ))

    try:
        context = pipeline.run(topic)
        console.print(f"\n[bold green]✅ 学习路径已生成！[/]")
        console.print(f"[dim]文件保存在: {output_dir}/[/]\n")

        # 显示预览
        if context.framework:
            console.print(Panel(
                context.framework.overview,
                title=f"📖 {context.framework.topic}",
                border_style="cyan",
            ))
            for stage in context.framework.stages:
                points = ", ".join(p.title for p in stage.points)
                console.print(f"  [bold]{stage.level}[/] - {stage.title}: {points}")

    except KeyboardInterrupt:
        console.print("\n[yellow]已取消[/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]错误: {e}[/]")
        logging.getLogger(__name__).exception("Pipeline 执行失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
