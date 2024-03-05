# EX 18
# print extended: https://lerner.co.il/2019/01/18/beyond-the-hello-world-of-pythons-print-function/
# context manager: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
# file-like string object

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

#
# dct = {'a': 1}
#
# print(dct.get('b',0))
# print(dct)
#
#





