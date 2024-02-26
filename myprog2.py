#!/usr/bin/env python3

from typing import Union


def myfunc(numbers: list[int] | tuple[int, str, int]) -> int:
    return numbers[0]


print(myfunc([10, 20, 30]))
print(myfunc((10, 20, 30)))
