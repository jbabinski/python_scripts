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

# EX 19
def passwd_to_dict(filename):
    """
    returns a dict with usernames and users' ids. Example:
    _launchservicesd:*:239:239::0:0:_launchservicesd:/var/empty:/usr/bin/false
    """
    users = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):    #ignore comments/blank lines
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
        return(users)


# print(passwd_to_dict('5_passwd.txt'))
import collections
def users_shell(filename):
    """
    returns a dict with shells and user logins. Example:
    _launchservicesd:*:239:239::0:0:_launchservicesd:/var/empty:/usr/bin/false
    """
    users_shells = collections.defaultdict(list)
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):    #ignore comments/blank lines
                user_info = line.strip().split(':')
                users_shells[user_info[-1]].append(user_info[0])
        return users_shells









