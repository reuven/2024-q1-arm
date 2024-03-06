import pytest
from count_vowels import count_vowels


@pytest.mark.parameterize()
def test_text(text, counts):
    assert count_vowels(text) == counts
