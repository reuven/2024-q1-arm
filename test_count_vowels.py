import pytest
from count_vowels import count_vowels


def test_text(text, counts):
    assert count_vowels(text) == counts
