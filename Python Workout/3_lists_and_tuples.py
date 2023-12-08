# Ex 9
import operator


def firstlast(seq):
    return seq[:1] + seq[-1:]  # need to use slices -> returns type it gets

# check: operator.itemgetter http://mng.bz/dyPQ
# check: collections.Counter http://mng.bz/rrBX


def sumindexes(seq):
    odd_indexes = []
    even_idexes = []

    for i, num in enumerate(seq):
        if i % 2 == 0:
            odd_indexes.append(num)
        else:
            even_idexes.append(num)
    return [sum(odd_indexes), sum(even_idexes)]


def addsubtract(seq):
    nums = []

    for i, num in enumerate(seq):
        if i % 2 == 0:
            nums.append(num)
        else:
            nums.append(-num)
    return [sum(nums)]


def myzip(*lists):
    final_list = []

    for i in range(len(lists[0])):
        this_list = []
        for seq in lists:
            this_list.append(seq[i])
        final_list.append(tuple(this_list))
    return final_list

# dict union: https://peps.python.org/pep-0584/
# EX 10

def mysum2(*items):

    if not items:
        output = ()
    output = items[0]

    for item in items[1:]:
        output += item

    return output


def mysum_bigger_than(base, *items):

    if not items or not base:
        output = ()
    output = items[0]
    for item in items[1:]:
        if item >= base:
            output += item

    return output


def sum_numeric(*nums):
    output = 0

    for num in nums:
        if str(num).isnumeric():
            output += int(num)

    return output


def concat_dicts(*dicts):
    keys = []
    concated_dict = dict()

    for dct in dicts:
        for key in dct.keys():
            keys.append(key)

    for key in keys:
        if keys.count(key) > 1:
            appended_vals = []
            for dct in dicts:
                appended_vals.append(dct.get(key))
            concated_dict.update({key: appended_vals})
        else:
            for dct in dicts:
                if dct.get(key):
                    concated_dict.update({key: dct.get(key)})

    return concated_dict




# EX 11
PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'},
{'first':'Zladimir', 'last':'Putin',
'email':'president@kremvax.ru'}
]

def alphabetize_names(PEOPLE):
    return sorted(PEOPLE, key=lambda x: (x.get('last'), x.get('first')))

# alternative:
# def alphabetize_names(PEOPLE):
#     return sorted(PEOPLE, key=operator.itemgetter('last', 'first'))


def sort_absolute(seq):
    return sorted(seq, key=lambda x: abs(x))


def sort_vowels(seq):
    return sorted(seq, key=lambda x: sum(1 for letter in x if letter in 'aeiou'))


def sort_sums(seq):
    return sorted(seq, key=lambda x: sum(item if str(item).isnumeric() else 0 for item in x))


# EX 12:
# collections.Counter: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter


words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter(word):
    return Counter(word).most_common(1)[0][1]
    # (1) - find the 1st most common word;
    # [0] get 1st element of tuple - result of most_common fun
    # [1] get 2nd element of the most common element, the first one is the word


def most_repeating_word(words):
    return max(words, key=most_repeating_letter)


def most_repeating_vowels(word):
    cnt = Counter()

    for letter in word:
        if letter in 'aeiou':
            cnt[letter] += 1

    return cnt.most_common(1)[0][1]


def most_repeating_word_vowels(words):
    return max(words, key=most_repeating_vowels)


# EX 13
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

#str.format https://docs.python.org/3/library/stdtypes.html#str.format
def format_sort_records(tuples):
    output = []
    output_format = "{1:10} {0:10} {2:5.2f}"  # {position in final string: length of that string}
    for person_details in sorted(tuples, key=operator.itemgetter(1, 0)):  # get tuple with 2nd,1st element
        output.append(output_format.format(*person_details))  # unpack tuple of values: https://pythonhow.com/what/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters/

    return output

from collections import namedtuple
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://stackoverflow.com/questions/25000159/how-to-cast-tuple-into-namedtuple
# https://stackoverflow.com/questions/50655608/formatting-a-string-with-a-namedtuple
# https://realpython.com/python-namedtuple/

def format_sort_records_v2(tuples):
    named_tuple = namedtuple('vips', ['first_name', 'last_name', 'time'])
    named_tuples = [named_tuple(*vip) for vip in tuples]

    output = []
    output_format = "{last_name:10} {first_name:10} {time:5.2f}"  # use aliases instead of indexes
    for person_details in sorted(named_tuples, key=lambda x: (x.last_name, x.first_name)):
        output.append(output_format.format(**person_details._asdict()))  # cast as dict, unpack with **

    return output


OSCARS = [('CODA', 'Sian Heder', 111),
          ('Belfast', 'Kenneth Branagh', 97),
          ('Dont Look Up', 'Adam McKay', 111)]


def sort_oscars(films):
    named_tuple = namedtuple('movies', ['title', 'director', 'time'])
    films_named_tuple = [named_tuple(*movie) for movie in films]

    output = []
    output_format = '{title:20} {director:20} {time:4}'
    axis_chosen = input('Select axis to sort by: title, director or time:\n')
    # for axis in axis_chosen.split(','):

    for movie_details in sorted(films_named_tuple, key=(lambda x: (getattr(x, axis_chosen), getattr(x, 'director')))):
        output.append(output_format.format(**movie_details._asdict()))

    for movie in output:
        print(movie)


def sort_oscars(films):
    named_tuple = namedtuple('movies', ['title', 'director', 'time'])
    films_named_tuple = [named_tuple(*movie) for movie in films]

    output = []
    output_format = '{title:20} {director:20} {time:4}'
    axis_chosen = input('Select axis to sort by: title, director or time. Split by comma (,) for mutliple layers:\n')
    # axis_chosen = "time,title"
    for axis in reversed(axis_chosen.split(',')):
        films_named_tuple = sorted(films_named_tuple, key=lambda x: getattr(x, axis))  # reverse from
    for movie_details in films_named_tuple:
        output.append(output_format.format(**movie_details._asdict()))

    for movie in output:
        print(movie)

sort_oscars(OSCARS)


# named_tuple = namedtuple('movies', ['title', 'director', 'time'])
# films_named_tuple = [named_tuple(*movie) for movie in OSCARS]
# print(getattr(films_named_tuple[0], 'title'))


# print(sorted(sorted(films_named_tuple, key=lambda x: getattr(x, 'title')), key=lambda x: getattr(x, 'time')))
