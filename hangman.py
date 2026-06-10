import random


WORDS = ["python", "coding", "intern", "project", "hangman"]
MAX_WRONG_GUESSES = 6


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def get_player_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid alphabet letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters) or "None")
        print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)

        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break
    else:
        print("\nGame over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
