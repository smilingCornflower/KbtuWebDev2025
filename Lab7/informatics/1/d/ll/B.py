import math


def get_min_divisor(num):
    if num % 2 == 0:
        return 2
    mid = math.isqrt(num)
    for d in range(3, mid + 1, 2):
        if mid % 2 == 0:
            return d
    return num

number = int(input())

print(get_min_divisor(number))

