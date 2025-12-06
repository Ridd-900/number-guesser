# Random number guesser program where the computer tries to guess the user's number
# The user can set the number range, and the computer makes repeated attempts
# Features: attempt counter, "higher/lower" hints, narrowing search range, no repeat guesses

# Get valid minimum number input
while True:
    try:
        min_num = int(input("Enter minimum number: "))
        break
    except ValueError:
        print("Error: Please enter a valid number. Try again.")

# Get valid maximum number input
while True:
    try:
        max_num = int(input("Enter maximum number: "))
        break
    except ValueError:
        print("Error: Please enter a valid number. Try again.")

# Swap if minimum > maximum
if min_num > max_num:
    min_num, max_num = max_num, min_num
    print(f'Range automatically adjusted to {min_num} to {max_num}')

import random

# Get valid user number within the range
valid_input = False
while not valid_input:
    try:
        user_number = int(input(f"Enter your number between {min_num} and {max_num}: "))
    except ValueError:
        print("Error: Please enter a valid number. Try again.")
        continue

    if min_num <= user_number <= max_num:
        valid_input = True
    else:
        print(f"Number must be between {min_num} and {max_num}. Try again.")

# Initialize attempts counter and search boundaries
attempts = 0
low = min_num
high = max_num

# First guess attempt
computer_guess = random.randint(low, high)
print(f'\nComputer\'s first guess: {computer_guess}')
attempts += 1

# Check if first guess is correct
if computer_guess == user_number:
    print(f'Congratulations! Your number {user_number} was guessed.')
    print(f'Attempts needed: {attempts}')
else:
    guessed_correctly = False

    while not guessed_correctly:
        # Generate new guess within current boundaries
        computer_guess = random.randint(low, high)
        attempts += 1
        print(f'\nAttempt {attempts}: {computer_guess}')

        if computer_guess == user_number:
            guessed_correctly = True
            print(f"\nThe computer guessed your number: {user_number}")
            print(f'Total attempts: {attempts}')
        else:
            print('The computer did not guess correctly.')

            # Provide hint and adjust search boundaries
            if computer_guess < user_number:
                print('Your number is higher.')
                low = computer_guess + 1
            else:
                print('Your number is lower.')
                high = computer_guess - 1







