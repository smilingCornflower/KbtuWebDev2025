input()
lst = [int(i) for i in input().split()]

print(sum(filter(lambda x: x >= 0, lst)))