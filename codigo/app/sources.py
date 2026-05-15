from abc import ABC, abstractmethod
from typing import Iterable, List

from .models import ContentItem


class ContentSource(ABC):
    @abstractmethod
    def fetch_items(self) -> List[ContentItem]:
        raise NotImplementedError


class BlogSource(ContentSource):
    def __init__(self, items: Iterable[ContentItem]) -> None:
        self._items = list(items)

    def fetch_items(self) -> List[ContentItem]:
        return list(self._items)


class ReleaseSource(ContentSource):
    def __init__(self, items: Iterable[ContentItem]) -> None:
        self._items = list(items)

    def fetch_items(self) -> List[ContentItem]:
        return list(self._items)
