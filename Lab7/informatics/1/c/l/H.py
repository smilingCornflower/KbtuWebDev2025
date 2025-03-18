import math

num = int(input())
for i in range(1, math.isqrt(num) + 1):
    if num % i == 0:
        print(i, end=' ')
print(num)
