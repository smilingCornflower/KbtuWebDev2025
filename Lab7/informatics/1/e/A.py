def min_of_four(a: int, b: int, c: int, d: int) -> int:
    return min([a, b, c, d])


numbers = list(map(int, input().split()))

print(min_of_four(numbers[0], numbers[1], numbers[2], numbers[3]))


