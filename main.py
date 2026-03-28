import logic

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
min_num, max_num, was_swapped = logic.check_range(min_num, max_num)
if was_swapped:
    print(f'Range automatically adjusted to {min_num} to {max_num}')

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

computer_guess, attempts = logic.first_attempt(low, high, attempts)
print(f'\nComputer\'s first guess: {computer_guess}')

# Check if first guess is correct
if computer_guess == user_number:
    print(f'Congratulations! Your number {user_number} was guessed.')
    print(f'Attempts needed: {attempts}')
else:
    guessed_correctly = False
    while not guessed_correctly:
        computer_guess, attempts = logic.computer_attempts(low, high, attempts)
        print(f'\nAttempt {attempts}: {computer_guess}')
        if computer_guess == user_number:
            guessed_correctly = True
            print(f"\nThe computer guessed your number: {user_number}")
            print(f'Total attempts: {attempts}')
        elif computer_guess < user_number:
            print('The computer did not guess correctly.')
            low, computer_guess = logic.hint_low(low, computer_guess)
            print('Your number is higher.')
        else:
            print('The computer did not guess correctly.')
            high, computer_guess = logic.hint_high(high, computer_guess)
            print('Your number is lower.')
