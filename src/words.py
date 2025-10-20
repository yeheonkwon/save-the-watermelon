"""
words.py - Load word list for the game
"""

import random
from pathlib import Path
from typing import List

# 기본 단어 리스트
DEFAULT_WORDS = [
    "watermelon", "python", "banana", "apple", "orange",
    "melon", "gardener", "sunshine", "island", "puzzle"
]

def load_words(path: str = None) -> List[str]:
    """Load words from file or return default list."""
    if path:
        p = Path(path)
    else:
        p = Path(__file__).resolve().parent / "words.txt"
    try:
        with p.open("r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        if words:
            return words
    except Exception:
        pass
    return DEFAULT_WORDS

def pick_random(words: List[str]) -> str:
    """Pick a random word."""
    return random.choice(words).lower()
