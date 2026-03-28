import random

# Swap if minimum > maximum
def check_range(min_num, max_num):
    was_swapped = False
    if min_num > max_num:
        min_num, max_num = max_num, min_num
        was_swapped = True
    return min_num, max_num, was_swapped

# First guess attempt
def first_attempt(low, high, attempts):
    computer_guess = random.randint(low, high)
    attempts += 1
    return computer_guess, attempts

# Generate new guess within current boundaries
def computer_attempts(low, high, attempts):
        computer_guess = random.randint(low, high)
        attempts += 1
        return computer_guess, attempts

# Provide hint and adjust search boundaries
def hint_low(low, computer_guess):
        low = computer_guess + 1
        return low, computer_guess
def hint_high(high, computer_guess):
        high = computer_guess - 1
        return high, computer_guess
