import pytest
from min_and_max import min_and_max


@pytest.mark.parametrize('input_values, expected_tuple',
                         [                                     # list of tuples to pass to each test
                             # (input_values, expected_tuple)
                             ([10, 20, 30, -5, -7], (-7, 30)),
                             ([10.5, 20.3, 30.7, -5.2, -7.1], (-7.1, 30.7)),
                             ([10.5, 20.3, 30.7, -5.2, -7.1], (111, 222)),
                             ('this is a ridiculous test'.split(), ('a', 'this'))
                         ])
def test_template(input_values, expected_tuple):
    assert min_and_max(input_values) == expected_tuple


# def test_simple():
#     assert min_and_max([10, 20, 30, -5, -7]) == (-7, 30)


# def test_floats():
#     assert min_and_max([10.5, 20.3, 30.7, -5.2, -7.1]) == (-7.1, 30.7)


# def test_strings():
#     assert (min_and_max('this is a ridiculous test'.split())) == ('a', 'this')


def test_empty():
    with pytest.raises(ValueError):
        min_and_max([])


# def test_not_empty():
#     with pytest.raises(ValueError):
#         min_and_max([10, 20, 30])
