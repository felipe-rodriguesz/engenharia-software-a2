from dataclasses import replace
from typing import Iterable, List

from .models import CarouselSlide


class ReviewHighlighter:
    def __init__(self, sensitive_terms: Iterable[str]) -> None:
        self._terms = [term.lower() for term in sensitive_terms]

    def mark(self, slides: Iterable[CarouselSlide]) -> List[CarouselSlide]:
        marked: List[CarouselSlide] = []
        for slide in slides:
            hits = [term for term in self._terms if term in slide.body.lower()]
            marked.append(replace(slide, highlights=hits))
        return marked
