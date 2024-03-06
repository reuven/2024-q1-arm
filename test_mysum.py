from mysum import mysum


def test_integers():
    assert mysum([10, 20, 30]) == 60


def test_floats():
    assert mysum([10.5, 20.5, 30.5]) == 61.5


def test_bad_floats():
    assert mysum([0.1, 0.2]) == 0.3
