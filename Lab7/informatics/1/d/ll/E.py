from math import log2

n = int(input())
i = log2(n)
if int(i) == i:
    print(int(i))
else:
    print(int(i) + 1)

