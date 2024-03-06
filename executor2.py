#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time
import random


def square(x):
    time.sleep(random.randint(0, 3))
    return x ** 2


with ThreadPoolExecutor(max_workers=10) as executor:
    all_results = executor.map(square, range(20))

    done, not_done = wait(
        all_results, return_when=FIRST_COMPLETED)

    for one_result in done:
        print(one_result.result())
