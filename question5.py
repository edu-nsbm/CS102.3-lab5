def main() -> None:
    count: int = 1
    total: int = 0

    while count <= 5:
        num: int = int(input("Enter Number: "))

        total += num
        count += 1

    print(f"{total = }")


if __name__ == "__main__":
    main()
