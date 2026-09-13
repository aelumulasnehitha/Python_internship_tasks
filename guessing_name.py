import random

print("Number Guessing Game")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess it!")
print("Enter 'q' anytime to quit.")

while True:
    user_input = input("Enter your guess: ")

    if user_input.lower() == "q":
        print("Game ended.")
        print("The correct number was:", secret_number)
        break

    try:
        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("Congratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number or 'q'.")