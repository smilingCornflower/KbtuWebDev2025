def main() -> None:
    MKAD_LENGTH = 109

    v = int(input())
    t = int(input())

    position = (v * t) % MKAD_LENGTH
    print(position if position >= 0 else MKAD_LENGTH + position)


if __name__ == "__main__":
    main()
