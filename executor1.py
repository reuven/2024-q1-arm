#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait


def square(x):
    return x ** 2


with ThreadPoolExecutor() as executor:
    all_results = []
    for one_number in range(10):
        one_result = executor.submit(square, one_number)
        all_results.append(one_result)

    done, not_done = wait(all_results)

    for one_result in done:
        print(one_result.result())
