def main() -> None:
    count: int = 1
    total: int = 0

    while count <= 10:
        curr_mark: int = int(input(f"Enter mark {count}: "))
        total += curr_mark
        count += 1

    avarage: float = total / 10

    print(f"{total = }")
    print(f"{avarage = }")
    print(f"{'Pass' if avarage >= 50 else 'Fail'}")


if __name__ == "__main__":
    main()
