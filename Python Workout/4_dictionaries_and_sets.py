# dicts: https://www.youtube.com/watch?v=p33CVV29OG8
# hash: https://en.wikipedia.org/wiki/Hash_function
# EX 14

MENU = {'fish': 1,
        'chicken': 2,
        'eggs': 2.3}


def restaurant(menu):
    total = 0.0
    while True:
        s = input('Select the product. Enter to quit\n')
        if s in menu.keys():
            total += menu[s]
            print(f'{s} added. Total is {total}')
        elif s:
            print(f'Item {s} not found.')
        else:
            break


PASS = {'user1': '1234',
        'user2': 'blah1'}


def pass_checker(pass_dict):
    user = input('Provide user name\n')
    password = input(f'Provide password for user {user}\n')
    if pass_dict[user] == password:
        print("Login successful")
    else:
        print('User x password combination not recognized')


TEMPERATURE = {'2023-03-15': 23,
               '2023-03-16': 24,
               '2023-03-17': 22}

from datetime import datetime, timedelta


def temp_checker(temp_dict):

    s = input('Provide date:\n')
    if s in temp_dict.keys():
        print(f'Temp on {s}: {temp_dict[s]}.\n')
        prev_date = (datetime.strptime(s, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
        next_date = (datetime.strptime(s, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        for dt in (prev_date, next_date):
            if dt in temp_dict.keys():
                print(f'Temp on {dt}: {temp_dict[dt]}\n')
            else:
                print(f'No data for {dt}')
    else:
        print("Date not found")


# dates: https://docs.python.org/3/library/datetime.html?#module-datetime
from datetime import date


BIRTHDAYS = {"Marian": date.fromisoformat('2019-01-01'),
             "Kleofas": date.fromisoformat('1921-05-05')}


def check_age(birthdays):

    s = input('Provide name to get age:\n')
    if s in birthdays.keys():
        print((datetime.now().date() - birthdays[s]).days)


# EX 15
# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict


def get_rainfall():
    rainfall = defaultdict(list)

    while True:
        city = input('Provide the city. Enter once finished:\n')
        if not city:
            break
        mm_rain = input('Rain in mm:\n')

        rainfall[city].append(int(mm_rain))
        # get(k, 0) -> 0 if not found, adding int to v

    for c, r in rainfall.items():
        print(f'Rain in {c}: {sum(r)/len(r):.2f} mm')

import re


regex = r'^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}.*\d{3} \d{4}$'


def error_logger(file):
    logs = defaultdict(list)

    with open(file, 'r') as f:
        for line in f.readlines():
            if re.match(regex, line) is not None:
                ip = re.search(r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}",
                               line)[0]
                error = re.search(r'.*\d{3} \d{4}', line)[0].split()[-2]
                print(ip)

            logs[error].append(ip)

    return logs


def char_counter(file):
    words_dict = {}

    with open(file, 'r') as f:
        chars = ''.join(char.lower() for char in f.read() if char not in ".,:[]?")
    for word in chars.split():
        words_dict[word] = int(words_dict.get(word, 0)) + 1

    return words_dict


# EX 16
def dictdiff(d1, d2):
    output = {}

    all_keys = d1.keys() | d2.keys()  # union of keys; '&' -> intersection
    for key in all_keys:
        if d1[key] != d2[key]:
            output[key] = [d1.get(key),
                           d2.get(key)]

    return output


def dictmerger(*dicts):
    output = {}
    for dct in dicts:
        output.update(dct)

    return output


def dictcreator(seq):
    output = {}

    if len(seq) % 2 == 0:
        for i, item in enumerate(seq, 0):
            print(i, item)
            if i % 2 == 0:
                output[seq[i]] = seq[i+1]

    return output


# # example fun
# def modulo_check(num=0):
#     return num % 2 == 0


def dict_partition(d, f):
    output_true = {}
    output_false = {}

    for k, v in d.items():

        if f(v):
            output_true[k] = v
        else:
            output_false[k] = v

    return [output_true, output_false]


# EX 17

