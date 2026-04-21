def main_b() -> None:
    count: int = 10

    while count >= 0:
        print(count)
        count -= 1


def main_a() -> None:
    count: int = 0

    while count <= 10:
        print(count)

        count += 1


if __name__ == "__main__":
    main_a()
    print()
    main_b()
