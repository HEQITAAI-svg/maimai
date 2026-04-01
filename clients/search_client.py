"""搜索客户端 - DuckDuckGo + GitHub API"""

from __future__ import annotations

import logging
from typing import Optional

import requests
from duckduckgo_search import DDGS

from models.schema import Resource

logger = logging.getLogger(__name__)


class SearchClient:
    """搜索引擎客户端，聚合 DuckDuckGo 和 GitHub 搜索"""

    def __init__(self, max_results: int = 5, github_token: str = ""):
        self.max_results = max_results
        self.github_token = github_token

    def search_articles(self, keywords: str) -> list[Resource]:
        """通过 DuckDuckGo 搜索技术文章"""
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(
                    f"{keywords} 教程 指南",
                    max_results=self.max_results,
                ))
            return [
                Resource(
                    title=r.get("title", ""),
                    url=r.get("href", ""),
                    type="article",
                    description=r.get("body", ""),
                )
                for r in results
                if r.get("href")
            ]
        except Exception as e:
            logger.warning(f"文章搜索失败 [{keywords}]: {e}")
            return []

    def search_videos(self, keywords: str) -> list[Resource]:
        """通过 DuckDuckGo 搜索视频"""
        try:
            with DDGS() as ddgs:
                results = list(ddgs.videos(
                    f"{keywords} tutorial",
                    max_results=self.max_results,
                ))
            return [
                Resource(
                    title=r.get("title", ""),
                    url=r.get("content", ""),
                    type="video",
                    description=r.get("description", ""),
                )
                for r in results
                if r.get("content")
            ]
        except Exception as e:
            logger.warning(f"视频搜索失败 [{keywords}]: {e}")
            return []

    def search_github(self, keywords: str) -> list[Resource]:
        """通过 GitHub API 搜索相关项目"""
        try:
            headers = {"Accept": "application/vnd.github.v3+json"}
            if self.github_token:
                headers["Authorization"] = f"token {self.github_token}"

            resp = requests.get(
                "https://api.github.com/search/repositories",
                params={
                    "q": keywords,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": self.max_results,
                },
                headers=headers,
                timeout=15,
            )
            resp.raise_for_status()
            items = resp.json().get("items", [])

            return [
                Resource(
                    title=f"{item['full_name']} ⭐{item.get('stargazers_count', 0)}",
                    url=item["html_url"],
                    type="github",
                    description=item.get("description", "") or "",
                )
                for item in items
            ]
        except Exception as e:
            logger.warning(f"GitHub 搜索失败 [{keywords}]: {e}")
            return []

    def search_all(self, keywords: str) -> list[Resource]:
        """搜索所有类型的资源"""
        resources = []
        resources.extend(self.search_articles(keywords))
        resources.extend(self.search_videos(keywords))
        resources.extend(self.search_github(keywords))
        return resources
