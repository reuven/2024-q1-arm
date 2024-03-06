import pytest
from count_vowels import count_vowels


@pytest.mark.parametrize('text, counts',
                         [
                             ('testing', {'a': 0, 'e': 1,
                              'i': 1, 'o': 0, 'u': 0}),
                             ('TESTING', {'a': 0, 'e': 1,
                              'i': 1, 'o': 0, 'u': 0}),
                             ('this is yet another test', {
                              'a': 0, 'e': 1, 'i': 1, 'o': 0, 'u': 0}),
                         ])
def test_text(text, counts):
    assert count_vowels(text) == counts
