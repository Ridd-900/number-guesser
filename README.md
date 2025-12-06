# Number Guesser

## Demo

![Number Guesser in Action] (screenshots/demo.png)
*the computer successfully guessing number 12 in 6 attempts*


A Python program where the computer tries to guess a number chosen by the user.

## Features
- Custom number range (user defines min and max)
- Computer makes intelligent guesses with "higher/lower" hints
- Search range narrows after each incorrect guess
- Attempt counter
- Error handling for invalid inputs
- No repeated guesses within the current range

## How It Works
1. User sets the number range
2. User thinks of a number within that range
3. Computer attempts to guess the number
4. After each wrong guess, computer gets a "higher/lower" hint
5. Computer uses hints to narrow down the search range
6. Program continues until the number is guessed

## Technologies Used
- Python 3
- Random module for number generation
- Exception handling for input validation

## Skills Demonstrated
- Algorithm design (adaptive search)
- User input validation
- Loop control structures
- Problem-solving through incremental improvements

## How to Run
`bash
python number_guesser.py
