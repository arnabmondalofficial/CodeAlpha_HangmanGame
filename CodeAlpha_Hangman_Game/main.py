import random

print("Welcome to Hangman")
print("Guess the word one letter at a time.")
print("You are allowed up to 6 incorrect attempts.\n")

# Predefined list of words
word_pool = ["python", "hangman", "computer", "programming", "developer"]

# Select a random word from the pool
target_word = random.choice(word_pool)

# Game state variables
guessed_characters = []
incorrect_attempts = 0
max_incorrect_attempts = 6

# Initialize display with underscores
revealed_word = ["_"] * len(target_word)

# Main game loop
while incorrect_attempts < max_incorrect_attempts and "_" in revealed_word:

    print("\nCurrent word:", " ".join(revealed_word))
    print(f"Remaining incorrect attempts: {max_incorrect_attempts - incorrect_attempts}")

    if guessed_characters:
        print("Guessed characters:", ", ".join(guessed_characters))
    else:
        print("Guessed characters: None")

    user_guess = input("Enter a letter: ").strip().lower()

    # Input validation
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Invalid input. Please enter a single alphabet character.")
        continue

    if user_guess in guessed_characters:
        print("This character has already been guessed.")
        continue

    guessed_characters.append(user_guess)

    # Check if the guessed character is in the word
    if user_guess in target_word:
        print("Correct guess.")

        for position in range(len(target_word)):
            if target_word[position] == user_guess:
                revealed_word[position] = user_guess
    else:
        print("Incorrect guess.")
        incorrect_attempts += 1

# Game result
print("\n----------------------------------")

if "_" not in revealed_word:
    print(f"Congratulations. You guessed the word '{target_word}'.")
else:
    print(f"Game over. The correct word was '{target_word}'.")

print("----------------------------------")