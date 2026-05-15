from typing import Dict, Iterable, List, Optional

from .models import ContentItem


class ContentRepository:
    def __init__(self) -> None:
        self._seen_ids = set()
        self._items: Dict[str, ContentItem] = {}

    def register_new_items(self, items: Iterable[ContentItem]) -> List[ContentItem]:
        new_items: List[ContentItem] = []
        for item in items:
            if not item.content_id or not item.url:
                raise ValueError("item must have content_id and url")
            if item.content_id in self._seen_ids:
                continue
            self._seen_ids.add(item.content_id)
            self._items[item.content_id] = item
            new_items.append(item)
        return new_items

    def get_item(self, content_id: str) -> Optional[ContentItem]:
        return self._items.get(content_id)
