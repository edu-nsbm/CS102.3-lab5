def main() -> None:
    count: int = 1
    largest: int = 0

    while count <= 3:
        curr_num: int = int(input(f"Enter number {count}: "))

        if curr_num > largest:
            largest = curr_num

        count += 1

    print(f"{largest = }")


if __name__ == "__main__":
    main()
