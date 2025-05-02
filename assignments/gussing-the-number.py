import random

secret_number = random.randint(1, 10)

# print(secret_number)
print("Guess a number between 1 and 10.")

try:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 10:
        raise ValueError("Guess must be between 1 and 10!")

    if guess == secret_number:
        print(f"Congratulations! You guessed the number correctly.")
    else:
        print("failed too guess Please try again")

except ValueError as e:
    print(f"Invalid input: Input Must be an integer {e}")
