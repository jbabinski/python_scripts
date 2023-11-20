# Ex 5 pig latin
from string import punctuation
import string

def pig_latin(word):
    word_capitalized = word[0].isupper()
    punct = ''

    if word[-1] in punctuation:
        punct = word[-1]
        word = word[:-1]

    if word[0].lower() in 'aeiou':
        new_word = word[1:] + 'way'
    else:
        new_word = word[1:] + word[0] + 'ay'
    if word_capitalized:
        return new_word.capitalize() + punct
    else:
        return new_word + punct


def pig_latin_alternative(word):
    word_capitalized = word[0].isupper()
    punct = ''

    if word[-1] in punctuation:
        punct = word[-1]
        word = word[:-1]

    if sum([1 for i in set(word.lower()) if i in 'aeiou']) > 1:
        new_word = word[1:] + 'way'
    else:
        new_word = word[1:] + word[0] + 'ay'
    if word_capitalized:
        return new_word.capitalize() + punct
    else:
        return new_word + punct


# Ex 6 pig latin sentence
def pig_latin_sentence(sentence):
    new_sentence = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            new_sentence.append(word[1:] + 'way')
        else:
            new_sentence.append(word[1:] + word[0] + 'ay')
    return ' '.join(new_sentence)


def make_dump_sentence(filepath):
    with open(filepath, 'r') as f:
        for i, line in enumerate(f.readlines()[:10]):
            print(f"Line {i} - take this word <<{line.split()[i]}>> and make dumb sentence!")


def transpose_list(word_list):
    array = [
        ['' for cols in range(len(word_list))]
        for rows in range(len(word_list[0].split()))
    ]
    new_list = []

    for line_no, line in enumerate(word_list):
        for word_no, word in enumerate(line.split()):
            array[word_no][line_no] = word

    for transposed_line in array:
        new_list.append(' '.join(transposed_line))

    return new_list

# Ex 7 Ubbi Dubbi


def ubbi_dubbi(word):
    new_word = []
    word_capitalized = word[0].isupper()

    for char in word:
        if char.lower() in 'aeiou':
            new_word.append('ub'+char)
        else:
            new_word.append(char)

    if word_capitalized:
        return ''.join(new_word).capitalize()
    else:
        return ''.join(new_word)


def remove_names(article, names=[]):
    splitted_art = article.split()
    article_lenght = len(splitted_art)
    article_redacted = []

    i = 0
    while i < article_lenght:
        for name in names:
            name_lenght = len(name.split())
            if name in ' '.join(splitted_art[i:i+name_lenght]):
                for x in range(0, name_lenght):
                    article_redacted.append('_')
                i += name_lenght
        article_redacted.append(splitted_art[i])
        i += 1
    return ' '.join(article_redacted)


def url_converter(url):
    new_url = []

    for char in url:
        if char in string.ascii_letters or char.isnumeric():
            new_url.append(char)
        else:
            new_url.append(f"%{hex(ord(char)).split('x')[1]}")
    return ''.join(new_url)


# unicode + UTF-8 https://nedbatchelder.com/text/unipain.html
# https://docs.python.org/3/howto/sorting.html#sortinghowto
# Ex 8
def strsort(text):
    return ''.join(sorted(text))


def sort_names():
    print(','.join(sorted('Tom Dick Harry'.split())))


def find_last_word(filepath):
    with open(filepath, 'r') as f:
        return sorted(f.read().split())[-1]


def find_longest_word(filepath):
    with open(filepath, 'r') as f:
        return sorted(f.read().split(), key=lambda word: len(word))[-1]


print(find_longest_word('string_text.txt'))
