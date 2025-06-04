import random
import os
from colorama import init, Fore, Style

from hangman.inputpkg.input_handler import select_category, ask_restart, get_user_input
from hangman.outputpkg.output_handler import (
    display_game_rules,
    display_current_word,
    display_used_letters,
    display_remaining_attempts,
    display_game_result,
)
from hangman.corepkg.word_selector import choose_random_word
from hangman.corepkg.logic import check_letter_in_word, check_game_over
from hangman.corepkg.repository import word_list_animals, word_list_foods, word_list_sports, hangman_pics
from hangman.corepkg.utils import clear_screen


init()

def play_game():
    clear_screen()
    display_game_rules()
    category = select_category()
    word = choose_random_word(category)
    guessed_letters = set()
    used_letters = []
    remaining_attempts = 6

    while True:
        display_current_word(word, guessed_letters)
        display_used_letters(used_letters)
        display_remaining_attempts(remaining_attempts)

        guess, is_vowel = get_user_input(used_letters)  
        if guess not in used_letters: 
            used_letters.append(guess)
        if check_letter_in_word(guess, word):
            guessed_letters.add(guess)
        else:
            if not is_vowel:  
                remaining_attempts -= 1

        over, success = check_game_over(word, guessed_letters, remaining_attempts)
        if over:
            display_remaining_attempts(remaining_attempts)
            display_game_result(word, success)
            break

    if ask_restart():
        play_game()

if __name__ == "__main__":
    play_game()