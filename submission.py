def main() -> None:
    num_1, num_2 = 0, 1

    count: int = 0

    while count <= 10:
        print(num_1)
        num_1, num_2 = num_2, num_1 + num_2

        count += 1


if __name__ == "__main__":
    main()
