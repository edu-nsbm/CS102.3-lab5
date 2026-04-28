def main() -> None:
    while True:
        num: int = int(input("Enter number: "))

        print(f"{num} is {'Even' if num % 2 == 0 else 'Odd'}")


if __name__ == "__main__":
    main()
