#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, wait
import time
import random


def square(x):
    return x ** 2


if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=10) as executor:
        all_results = executor.map(square, range(20))

        for one_result in all_results:
            print(one_result)
