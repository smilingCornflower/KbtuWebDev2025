a = int(input())
b = int(input())
a += (a % 2)

for i in range(a, b + 1, 2):
    print(i, end=' ')
