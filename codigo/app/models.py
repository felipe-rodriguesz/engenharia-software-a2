from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class ContentItem:
    content_id: str
    title: str
    url: str
    published_at: datetime
    body: str
    source: str


@dataclass(frozen=True)
class CarouselSlide:
    index: int
    title: str
    body: str
    highlights: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class CarouselScript:
    content_id: str
    slides: List[CarouselSlide]
    strategy_name: str
