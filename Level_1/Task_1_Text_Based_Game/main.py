
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nGuess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Correct! You win!")
                print(f"Attempts: {attempts}")
                break

        except ValueError:
            print("Invalid input! Enter a whole number.")

while True:
    play_game()
    again = input("Play again? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("Thanks for playing!")
        break
