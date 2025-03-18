import math


n = int(input())

for i in range(1, n + 1):
    root = math.isqrt(i)
    if root * root == i:
        print(i)