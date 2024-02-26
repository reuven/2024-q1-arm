#!/usr/bin/env python3

from typing import Union, Iterable


def myfunc(numbers: Iteratable[int]) -> int:
    return numbers[0]


print(myfunc([10, 20, 30]))
print(myfunc((10, 20, 30)))
