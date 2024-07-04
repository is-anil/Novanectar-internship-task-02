import random

# List of predefined words
WORDS = [
    "python", "hangman", "challenge", "programming", "developer",
    "interface", "software", "algorithm", "function", "variable"
]

HANGMAN_PICS = [
    '''
       +---+
       |   |
           |
           |
           |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    ''', '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    '''
]

def get_random_word():
    return random.choice(WORDS)

def display_hangman(misses):
    print(HANGMAN_PICS[misses])

def display_progress(word, guesses):
    display_word = ''.join([letter if letter in guesses else '_' for letter in word])
    print(' '.join(display_word))

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        else:
            return guess

def play_game():
    word = get_random_word()
    correct_guesses = set()
    missed_guesses = set()
    misses = 0
    max_misses = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while misses < max_misses:
        display_hangman(misses)
        display_progress(word, correct_guesses)

        guess = get_guess()

        if guess in correct_guesses or guess in missed_guesses:
            print(f"You already guessed '{guess}'. Try another letter.")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            correct_guesses.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            missed_guesses.add(guess)
            misses += 1

        if set(word) == correct_guesses:
            display_progress(word, correct_guesses)
            print("Congratulations! You've guessed the word!")
            break
    else:
        display_hangman(misses)
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_game()
