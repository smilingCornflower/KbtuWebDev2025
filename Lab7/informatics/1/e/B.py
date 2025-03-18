def pow_(number: float, power: float) -> float:
    return number ** power


a, n = map(float, input().split())

print(pow_(a, n))
