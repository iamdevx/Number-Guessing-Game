# Number Guessing Game

A simple Python console game where the player has up to 10 attempts to guess a randomly generated number between 1 and 100.

## Features

* Random number generation
* Higher/Lower hints
* Input validation using `try-except`
* Range validation (1–100)
* Attempt counter
* Win and lose conditions
* Invalid inputs do not consume attempts
* Play Again option
* Validation for replay input (`y/n`)

## Concepts Used

* Python
* Variables
* Loops (`while`)
* Conditional Statements
* Exception Handling
* Random Module
* User Input Validation

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run:

```bash
python number_guessing_game.py
```

## Example Gameplay

```text
Welcome to the Number Guessing Game!
You have 10 chances to guess the correct number between 1 and 100.

Let's Begin!

Attempt 1/10
What's your guess?: hello
Please enter a valid number!

Attempt 1/10
What's your guess?: 150
Please enter a number between 1 and 100!

Attempt 1/10
What's your guess?: 50
Whoops! Go HIGHER.

9 attempts remaining.

Play again? (yes/no): maybe
Please enter only 'yes' or 'no'.

Play again? (yes/no): yes
```

## Future Improvements

* Difficulty levels (Easy, Medium, Hard)
* Score system
* Previous guess tracking
* Hot/Cold hints
* Game statistics
