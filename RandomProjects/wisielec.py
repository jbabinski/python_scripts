# 1. lista słów
# 2. input usera
# 3. dodanie pętli
# 4. check, czy litera w słowie

import random
import requests
import re
from bs4 import BeautifulSoup

tries, used_letters = 1, []

r = requests.get('https://www.ef.pl/przewodnik-po-angielskim/listy-slow-angielskich/1000-slow/')
page = BeautifulSoup(r.content, 'html.parser')
raw_list = str(page.find("div", class_="field-item even")
               ).split('<br/>')[1:-1]
list_of_words = re.findall('[a-z]{3,}', ","
                           .join(raw_list)
                           )

random_no = random.randint(0, len(list_of_words)-1)
random_word = list_of_words[random_no]

random_word_hashed = '#' * len(random_word)
random_word_hashed_list = [letter for letter in random_word_hashed]
max_tries = len(set(random_word)) + 5

while tries <= max_tries:
    letter_input = input(f'Próba # {tries}/{max_tries} \nPodaj literę....\n')
    print(f'Podałeś literę >> {letter_input} <<')

    if letter_input in used_letters:
        print('Użyłeś już tej litery, spróbuj jeszcze raz. \n')
    elif len(letter_input) > 1:
        print('Podaj jedną literę.\n')
    elif not re.search('[A-Za-z]', letter_input):
        print('Niedozwolony znak, spróbuj podobnie')
    else:
        used_letters.append(letter_input)
        if letter_input in random_word:
            for n, letter in enumerate([let for let in random_word]):
                if letter == letter_input:
                    random_word_hashed_list[n] = letter
        else:
            print('To nie ta litera! Spróbuj jeszcze raz\n')
        print(''.join(random_word_hashed_list))

        if '#' not in random_word_hashed_list:
            print('WYGRANA!')
            tries = max_tries

        if tries == max_tries:
            if '#' in random_word_hashed_list:
                print(f'PRZEGRANA! Chodziło o {random_word}')

        tries += 1
