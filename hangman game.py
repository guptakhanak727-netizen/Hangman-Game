import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "computer", "developer", "program", "keyboard"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words)
    
    # Track the letters that the player has guessed
    guessed_letters = []
    
    # Track the number of incorrect guesses
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You can make up to {max_incorrect} incorrect guesses.")

    # 2. Main game loop
    while incorrect_guesses < max_incorrect:
        # Create the current display string with underscores and guessed letters
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord to guess: " + display_word.strip())
        print(f"Remaining incorrect guesses allowed: {max_incorrect - incorrect_guesses}")
        
        # Check if the player has guessed the complete word
        if "_" not in display_word:
            print("\nCongratulations! You won!")
            print(f"The word was indeed: {secret_word}")
            break

        # 3. Get player input
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.")
            continue

        # Add the valid new guess to the tracked list
        guessed_letters.append(guess)

        # 4. Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    # 5. Handle game over state if the user runs out of attempts
    if incorrect_guesses == max_incorrect:
        print("\nGame Over! You've run out of guesses.")
        print(f"The correct word was: {secret_word}")

# Start the game
if __name__ == "__main__":
    play_hangman()