# Without using any string methods, try to print the following:
# 123...n
# example:
# n = 5
# 12345

n = int(input())

for i in range(1, n + 1):
    print(i, end="")
