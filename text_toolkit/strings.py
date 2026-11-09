"""String utility functions."""

import re


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Example: "Hello World!" -> "hello-world"
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def is_palindrome(text: str) -> bool:
    """Check if text reads the same forwards and backwards.

    Ignores spaces, punctuation, and case.
    Example: "A man a plan a canal Panama" -> True
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    """Count the number of words in text."""
    return len(text.split())


def reverse_words(text: str) -> str:
    """Reverse the order of words in text.

    Example: "hello world" -> "world hello"
    """
    return " ".join(text.split()[::-1])