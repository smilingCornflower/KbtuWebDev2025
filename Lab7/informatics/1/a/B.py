def next_and_previous_numbers(number: int) -> None:
    print(f"The next number for the number {number} is {number + 1}.")
    print(f"The previous number for the number {number} is {number - 1}.")


def main() -> None:
    number = int(input())
    next_and_previous_numbers(number)


if __name__ == "__main__":
    main()
