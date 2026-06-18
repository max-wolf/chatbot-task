import json
from dataclasses import dataclass
from typing import List


@dataclass
class FAQ:
    id: int
    question: str
    answer: str


def load_faqs(path: str) -> List[FAQ]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [FAQ(**item) for item in data]