import time


def main() -> None:
    no_of_seconds: int = int(input("Enter no of seconds: "))

    count = 0

    while count <= no_of_seconds:
        time.sleep(1)
        print(no_of_seconds - count)
        count += 1


if __name__ == "__main__":
    main()
