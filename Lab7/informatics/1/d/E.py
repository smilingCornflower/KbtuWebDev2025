input()
lst = [int(i) for i in input().split()]

flag = False
for i in range(1, len(lst)):
    if lst[i - 1] * lst[i] > 0:
        flag = True

if flag:
    print('YES')
else:
    print('NO')