#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait


def square(x):
    if x == 4:
        raise TypeError('I hate 4!')
    return x ** 2


with ThreadPoolExecutor(max_workers=10) as executor:
    all_results = []
    for one_number in range(20):
        one_result = executor.submit(square, one_number)
        all_results.append(one_result)

    done, not_done = wait(all_results)

    for one_result in done:
        print(one_result.result())
