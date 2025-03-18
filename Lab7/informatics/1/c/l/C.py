import math


def is_perfect_square(num):
    root = math.isqrt(num)
    return root * root == num


a = int(input())
b = int(input())

for i in range(a, b + 1):
    if is_perfect_square(i):
        print(i, end=' ')

