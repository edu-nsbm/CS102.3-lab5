def main() -> None:
    count: int = 1
    total: int = 0

    while count <= 10:
        total += count
        count += 1

    print(f"{total = }")


if __name__ == "__main__":
    main()
