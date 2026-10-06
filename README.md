# Hangman-Game

A simple, lightweight console-based implementation of the classic Hangman word-guessing game built using Python.

## Goal
The goal of the project is to guess a randomly chosen secret word one letter at a time within a limited number of incorrect attempts.

## Features
* **Simplified Scope:** Uses a predefined static pool of 5 words (no external API or file reading required).
* **Attempt Tracking:** The player is allowed a maximum of 6 incorrect guesses before losing.
* **Basic Console Input/Output:** Runs entirely within the command-line interface with no visual or audio dependencies.
* **Input Validation:** Prevents penalties for entering invalid text (numbers, symbols, or multiple characters) or re-entering previously guessed letters.

## Core Programming Concepts Demonstrated
* `random` module for dynamic word selection.
* `while` loop to maintain the continuous interactive game loop.
* `if-else` branching logic for validating inputs and handling structural match validation.
* `strings` and `lists` data types to manage the target secret characters and tracking logs.

## Prerequisites
To run this application, you only need Python installed on your system.
* Python 3.x is highly recommended.

## How to Run

1. Copy the game code into a file named `hangman.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Execute the script using the following command:

```bash
python hangman.py
```

## How to Play
1. The game will automatically select a random word and display it as hidden underscores (e.g., `_ _ _ _ _ _`).
2. Type a single letter at the prompt and press `Enter`.
3. If the letter is part of the secret word, its position will be revealed.
4. If the letter is incorrect, your remaining lives will decrease by one.
5. Win the game by uncovering all letters before running out of attempts.
