# EX 18
# print extended: https://lerner.co.il/2019/01/18/beyond-the-hello-world-of-pythons-print-function/
# context manager: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
# file-like string object
import glob
import string


def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line


# using stringIO as file for testing:
# from io import StringIO
#
# output = StringIO()
# output.write('asdf\n')
#
# print(output.getvalue())

def numeric_finder(filename):
    numeric_items = []
    with open(filename) as f:
        for line in f.readlines():
            for item in line.split():
                if item.isnumeric():
                    numeric_items.append(float(item))
    return sum(numeric_items)


def column_multiplier(filename):
    total = []
    with open(filename) as f:
        for line in f.readlines():
            line_splitted = line.split()
            if line_splitted[0].isnumeric() and line_splitted[1].isnumeric():
                total.append(float(line_splitted[0]) * float(line_splitted[1]))

    return sum(total)


def count_vowels(filename):
    vowels = 'aeiou'
    vowel_dict = {}
    with open(filename) as f:
        for line in f.readlines():
            for char in line:
                if char in vowels:
                    vowel_dict[char] = vowel_dict.get(char, 0) + 1

    return vowel_dict


# EX 19
def passwd_to_dict(filename):
    """
    returns a dict with usernames and users' ids. Example:
    _launchservicesd:*:239:239::0:0:_launchservicesd:/var/empty:/usr/bin/false
    """
    users = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):  # ignore comments/blank lines
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
        return (users)


# print(passwd_to_dict('5_passwd.txt'))
import collections


def users_shell(filename):
    """
    returns a dict with shells and user logins. Example:
    _launchservicesd:*:239:239::0:0:_launchservicesd:/var/empty:/usr/bin/false
    """
    users_shells = collections.defaultdict(list)  # create doct where default value is list
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):  # ignore comments/blank lines
                user_info = line.strip().split(':')
                users_shells[user_info[-1]].append(user_info[0])
        return users_shells


def user_data_details(filename):
    users_data = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                user_info = line.strip().split(':')
                users_data[user_info[0]] = {'user_id': user_info[2]
                    , 'home_dir': user_info[-2]
                    , 'shell': user_info[-1]}
        return users_data


# EX 20
def wordcount(filename):
    chars = 0
    words = 0
    lines = 0
    unique_words = set()
    with open(filename) as f:
        for line in f:
            lines += 1
            chars += len(line)
            words_in_line = line.split()
            words += len(words_in_line)
            for word in words_in_line:
                unique_words.update(word)
        return ({'No. of characters': chars,
                 'No. of lines': lines,
                 'Unique words': len(unique_words),
                 'Words': words})


def count_words_in_string(filename):
    words_to_find = str(input('Which words you want to find separated by space.\n')).split(' ')
    dct = {w: 0 for w in words_to_find}
    with open(filename) as f:
        for line in f:
            for word in words_to_find:
                for item in line.split():
                    if word.lower() in item.lower():
                        dct[word] += 1
        return dct


# print(count_words_in_string('string_text.txt'))

# https://docs.python.org/3/library/os.html#os.stat
import os


def check_file_sizes(files):
    file_sizes = {}
    for file in files:
        file_sizes[file] = os.stat(file).st_size
    return file_sizes


import os


def letter_counter(folder_path):
    files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}
    for file in files:
        with open(file) as f:
            for line in f:
                for letter in line.lower():
                    if letter in string.ascii_lowercase:
                        alphabet_dict[letter] += 1

    return (sorted(alphabet_dict,
                   key=alphabet_dict.get,
                   reverse=True)[:5])


# EX 21
import os

folder_path = 'text_files'
filename = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

# find longest word in file
def find_longest_word(file) -> str:
    with open(file, 'r', encoding="utf8") as f:
        longest_word = ''
        for line in f:  # can be tweaked to replace links and commas, dots etc.
            for word in line.split():
                if 'http' not in word and len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def find_all_longest_words(folderpath) -> dict:
    filenames = [os.path.join(folderpath, file) for file in os.listdir(folderpath) if file.endswith('.txt')]
    longest_word = []

    for file in filenames:
        longest_word.append(find_longest_word(file))

    return dict(zip(filenames, longest_word))  # changed to comprehension in nex example


# files and hashes
from hashlib import md5

dir = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

def hash_file(file) -> str:
    with open(file, 'r', encoding='utf8') as f:
        str_data = f.read().strip().encode('utf8')  # has to be encoded for hashing to work
        return md5(str_data).hexdigest()  # https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest


def hash_folder(folder_path):
    return {
        filename:  # string with file we're looking for
        hash_file(os.path.join(folder_path, filename))  # hash for full path to given file
        for filename in os.listdir(folder_path)  # list with all files within that folder
        if filename.endswith('.txt')  # given it's a text file
    }

# directory stats
import os
import datetime

def dir_stats():
    dirs = input('Provide folder to check stats on:\n')
    now = datetime.datetime.now()
    try:
        for item in os.listdir(dirs):
            file_modtime = datetime.datetime.fromtimestamp(os.stat(f'E:\Godot\{item}').st_mtime)
            diff = (now - file_modtime).seconds
            print(f'{item}: last modified {diff} seconds ago.')
    except FileNotFoundError:
        print('File not found')

# server logs
import re

errors = dict()

with open('Repozytoria/python_scripts/Python Workout/text_files/http_logs.txt', 'r') as f:
    for line in f.readlines():
        error_type = re.findall(r'" [0-9]{3}', line)[0].split()[-1]
        if error_type in errors:
            errors[error_type] += 1
        else:
            errors[error_type] = 1
