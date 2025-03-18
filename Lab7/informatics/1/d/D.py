input()
lst = [int(i) for i in input().split()]

print(sum([lst[i-1] < lst[i] for i in range(1, len(lst))]))