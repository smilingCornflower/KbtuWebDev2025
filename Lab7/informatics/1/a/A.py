# Calc hypotenuse from two numbers

def get_hypotenuse(a: int | float, b: int | float) -> float:
    return (a ** 2 + b ** 2) ** 0.5


def main():
    a = int(input())
    b = int(input())

    hypotenuse = get_hypotenuse(a, b)
    print(hypotenuse)


if __name__ == "__main__":
    main()