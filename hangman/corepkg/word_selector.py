import random
from hangman.corepkg.repository import word_list_animals, word_list_foods, word_list_sports

def choose_random_word(catedory):
    if catedory == "1":
        return random.choice(word_list_animals)
    elif catedory == "2":
        return random.choice(word_list_foods)
    elif catedory == "3":
        return random.choice(word_list_sports)