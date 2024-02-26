def mysum(numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total


print(mysum([10, 20, 30]))
print(mysum([10, 20.5, 30]))
print(mysum([10, 'abcd', 30]))
print(mysum(10, 20, 30)
