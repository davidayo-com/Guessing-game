# Guessing-game

Welcome to the Guessing Game! This is a simple number guessing game where the player tries to guess a randomly generated number within a specified range.

## Table of Contents

- [Guessing-game](#guessing-game)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

The Guessing Game is a fun and interactive game where the player needs to guess a number chosen by the computer. The computer will provide hints whether the guessed number is too high, too low, or correct.

## Features

- Random number generation within a specified range
- User-friendly input prompts and validation
- Feedback on each guess (too high, too low, or correct)
- Count of attempts to guess the correct number

## Installation

To run this game on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/guessing-game.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd guessing-game
    ```

3. **Ensure you have Python installed:**

    The game requires Python 3.x. You can download Python from [python.org](https://www.python.org/).

## Usage

1. Run the script using Python.

    ```bash
    python guessing_game.py
    ```

2. Follow the on-screen prompts to play the game.

3. Enter your guess and the game will provide feedback.

4. Continue guessing until you find the correct number.

Example:

```bash
$ python guessing_game.py
Welcome to the Guessing Game!
I have chosen a number between 1 and 100. Can you guess what it is?
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Correct! You've guessed the number in 3 attempts.
