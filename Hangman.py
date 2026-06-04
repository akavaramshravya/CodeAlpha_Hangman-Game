import random

def play_hangman():
    # 1. Setup the game data
    word_bank = ["python", "coding", "program", "mystery", "jupiter"]
    secret_word = random.choice(word_bank)
    
    # Track guessed letters using a list of underscores
    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []  # Keeps track of all unique guesses
    incorrect_guesses_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the secret word, one letter at a time.")
    
    # 2. Main game loop
    while incorrect_guesses_left > 0 and "_" in guessed_word:
        print("\n" + "="*30)
        print(f"Word to guess: {' '.join(guessed_word)}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Letters guessed so far: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        
        # 3. Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter!")
            continue
            
        # Add to the tracked guesses
        guessed_letters.append(guess)
        
        # 4. Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the guessed_word list with the correctly guessed letter
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # 5. Game Over conditions
    print("\n" + "="*30)
    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {secret_word.upper()}")
    else:
        print(f"Game Over! You ran out of guesses. The word was: {secret_word.upper()}")

# Start the game
if __name__ == "__main__":
    play_hangman()