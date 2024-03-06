#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor


def square(x):
    return x ** 2


with ThreadPoolExecutor() as executor:
    for one_number in range(10):
        one_result = executor.submit(square, one_number)
        print(one_result)
