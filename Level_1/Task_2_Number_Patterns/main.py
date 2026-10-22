
def increasing_pattern(rows):
    print("\nPattern 1: Increasing Numbers")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def repeated_number_pattern(rows):
    print("\nPattern 2: Repeated Row Numbers")
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()


def decreasing_pattern(rows):
    print("\nPattern 3: Decreasing Numbers")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def main():
    print("===== NUMBER PATTERN GENERATOR =====")

    try:
        rows = int(input("Enter the number of rows (1-10): "))

        if rows < 1 or rows > 10:
            print("Please enter a number between 1 and 10.")
            return

        increasing_pattern(rows)
        repeated_number_pattern(rows)
        decreasing_pattern(rows)

    except ValueError:
        print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()
