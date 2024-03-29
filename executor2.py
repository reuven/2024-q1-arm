#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time
import random


def square(x):
    return x ** 2


with ThreadPoolExecutor(max_workers=10) as executor:
    all_results = executor.map(square, range(20))

    for one_result in all_results:
        print(one_result)
