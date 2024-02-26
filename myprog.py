from typing import Sequence, Iterable


# def mysum(numbers: Sequence[int | float]) -> int | float:
def mysum(numbers: Iterable[int | float]) -> int | float:
    total: float = 0

    for one_number in numbers:
        total += one_number

    return total


print(mysum([10, 20, 30]))
print(mysum((10, 20, 30)))
print(mysum({10, 20, 30}))
print(mysum([10, 20.5, 30]))
# print(mysum([10, 'abcd', 30]))
# print(mysum(10, 20, 30))
