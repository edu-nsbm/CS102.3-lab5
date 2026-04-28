# Write a python program to calculate factorial of a user-given number.

def main() -> None:
    num: int = int(input("Enter number: "))
    factorial: int = 1

    if num < 0:
        print("Cannot find factorial for negative integers")
    else:
        while num > 1:
            factorial *= num
            num -= 1

        print(f"{factorial = }")


if __name__ == "__main__":
    main()
