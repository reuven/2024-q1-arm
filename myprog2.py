#!/usr/bin/env python3

from typing import Union


def myfunc(numbers: Union[list, tuple]) -> int:
    return numbers[0]


print(myfunc([10, 20, 30]))
