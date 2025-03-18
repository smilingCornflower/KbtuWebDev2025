input()
lst = [int(i) for i in input().split()]
print(*filter(lambda x: x % 2 == 0, lst))