
import random


available_words = ["apple", "banana", "orange", "strawberry", "grape"]

def get_random_word():
    return random.choice(available_words)

def display_board(missed_letters, correct_letters, secret_word):
    print("Missed letters: ", end="")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

def get_guess():
    return input("Guess a letter: ")

def is_word_guessed(secret_word, correct_letters):
    for letter in secret_word:
        if letter not in correct_letters:
            return False
    return True

def play_game():
    secret_word = get_random_word()

    missed_letters = []
    correct_letters = []

    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess()

        if guess in secret_word:
            correct_letters.append(guess)
        else:
            missed_letters.append(guess)

        if len(missed_letters) >= 6:
            print("You lose! The word was " + secret_word)
            break

        if is_word_guessed(secret_word, correct_letters):
            print("You win! The word was " + secret_word)
            break

play_game()
