#!/usr/bin/env python3

from typing import Union, Iterable, Sequence


def myfunc(numbers: Sequence[int]) -> int:
    return numbers[0]


print(myfunc([10, 20, 30]))
print(myfunc((10, 20, 30)))
