from typing import Iterable, Mapping

from .models import ContentItem
from .sources import BlogSource, ContentSource, ReleaseSource


class SourceFactory:
    def create(self, source_type: str, config: Mapping[str, Iterable[ContentItem]]) -> ContentSource:
        if source_type == "blog":
            return BlogSource(config.get("items", []))
        if source_type == "release":
            return ReleaseSource(config.get("items", []))
        raise ValueError(f"Unknown source type: {source_type}")
