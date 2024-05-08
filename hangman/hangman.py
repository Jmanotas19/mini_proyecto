import random
import string

from hangman_diagram import lives_dict_visual
from hangman_words import *


def get_valid_word(word_list):
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(word_list)
    return word.upper()


def hangman():
    print("Welcome to Hangman!".center(40, "="))
    word = get_valid_word(words)
    guessed_letters = set()
    alphabet = set(string.ascii_uppercase)
    life = 7

    while life > 0:
        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print(lives_dict_visual[life])
        print(f"Word: {' '.join(word_list)}")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word!")
            break

        print(
            f"You have {life} lives remaining and you have used these letters: {' '.join(guessed_letters)}"
        )

        user_letter = input("Choose a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word:
                print("Good guess!")
            else:
                life -= 1
                print(f"\nSorry, '{user_letter}' is not in the word.")
        elif user_letter in guessed_letters:
            print("\nYou've already guessed that letter. Please choose another one.")
        else:
            print("\nInvalid input. Please enter a valid letter.")

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word!")
    else:
        print(lives_dict_visual[life])
        print(f"\nGame over! You ran out of lives. The word was: {word}")


hangman()
