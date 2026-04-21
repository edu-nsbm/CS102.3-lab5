def main() -> None:
    while True:
        name: str = input("Enter your name. (stop to end): ")

        if name == "stop":
            break
        else:
            print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
