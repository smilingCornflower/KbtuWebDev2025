def xor(a: int, b: int) -> int:
    return int(a != b)

a, b = map(int, input().split())
print(xor(a, b))