#!/usr/bin/env python3

def count_vowels(text):
    output = dict.fromkeys('aeiou', 0)

    for one_character in text.lower():
        if one_character in output:
            output[one_character] += 1

    return output
