n = int(input())

count = 0
for _ in range(n):
    i = int(input())
    if i == 0:
        count += 1
print(count)