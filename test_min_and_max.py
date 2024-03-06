from min_and_max import min_and_max


def test_simple():
    assert min_and_max([10, 20, 30, -5, -7]) == (-7, 30)
