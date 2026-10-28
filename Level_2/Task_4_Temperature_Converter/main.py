
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose conversion (1 or 2): ").strip()

    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C = {result:.2f}°F")

        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F = {result:.2f}°C")

        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")


if __name__ == "__main__":
    main()
1