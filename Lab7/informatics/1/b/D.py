number = int(input())


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


print(sign(number))