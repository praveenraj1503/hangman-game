import random

def hangman():
    # List of words for the game
    words = ["python", "hangman", "programming", "developer", "software"]

    # Randomly select a word from the list
    secret_word = random.choice(words)
    
    # Create a placeholder for the guessed word
    guessed_word = ["_" for _ in secret_word]

    # Set the limit for incorrect guesses
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    # Store guessed letters
    guessed_letters = set()

    print("Welcome to Hangman! Try to guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", " ".join(guessed_word))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Prompt the player to guess a letter
        try:
            guess = input("Enter a letter: ").strip().lower()
        except (EOFError, OSError):
            print("An error occurred while reading input. Please try again.")
            guess = None  # Set guess to None to prompt again

        # Validate input
        if not guess:
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for idx, char in enumerate(secret_word):
                if char == guess:
                    guessed_word[idx] = guess

            # Check if the player has guessed the whole word
            if "_" not in guessed_word:
                print("\nCongratulations! You've guessed the word:", secret_word)
                return
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    print("\nYou've run out of guesses. The word was:", secret_word)

# Run the game
if __name__ == "__main__":
    hangman()
