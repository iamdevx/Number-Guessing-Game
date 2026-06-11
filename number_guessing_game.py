from random import randint

random_number = randint(1, 100)
attempts = 0
max_attempts = 10

print("\nWelcome to the Number Guessing Game!")
print("You have 10 chances to guess the correct number between 1 and 100.")
print("\nLet's Begin!")

while attempts < max_attempts:

    print(f"\nAttempt {attempts + 1}/{max_attempts}")

    try:
        user_number = int(input("What's your guess?: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if not 1 <= user_number <= 100:
        print("Please enter a number between 1 and 100!")
        continue

    attempts += 1

    if user_number == random_number:
        print(f"\nYou guessed the right number: {random_number}!")
        print("Congratulations!")
        break

    elif user_number > random_number:
        print("Whoops! Go LOWER.")

    else:
        print("Whoops! Go HIGHER.")

    print(f"{max_attempts - attempts} attempts remaining.")

else:
    print(f"\nGame Over! The number was {random_number}.")

print("\nThanks for playing!")



