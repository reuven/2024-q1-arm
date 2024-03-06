#!/usr/bin/env python3

def min_and_max(numbers):
    min_number = numbers[0]
    max_number = numbers[0]

    for one_number in numbers:
        if one_number < min_number:
            min_number = one_number
        if one_number > max_number:
            max_number = one_number

    return min_number, max_number
