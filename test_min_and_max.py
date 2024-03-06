import pytest
from min_and_max import min_and_max


def test_simple():
    assert min_and_max([10, 20, 30, -5, -7]) == (-7, 30)


def test_floats():
    assert min_and_max([10.5, 20.3, 30.7, -5.2, -7.1]) == (-7.1, 30.7)


def test_empty():
    with pytest.raises(ValueError):
        min_and_max([])
