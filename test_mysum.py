from mysum import mysum


def test_integers():
    assert mysum([10, 20, 30]) == 60


def test_floats():
    assert mysum([10.5, 20.5, 30.5]) == 61.5
