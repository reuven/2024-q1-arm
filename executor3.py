#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
import time
import random


def square(x):
    time.sleep(random.randint(0, 3))
    return x ** 2


if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=10) as executor:
        all_results = []
        for one_number in range(20):
            one_result = executor.submit(square, one_number)
            all_results.append(one_result)

        done, not_done = wait(all_results)

        for one_result in done:
            print(one_result.result())
