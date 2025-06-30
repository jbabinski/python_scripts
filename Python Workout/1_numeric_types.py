# Ex 1: guessing game -
import random

def guessing_game(tries=3):
    num = random.randint(0, 10)

    while True:
        for try_no in range(tries):
            s = int(input(f"Try no {try_no}. Choose a number between 1 and 10.\n"))

            if s > num:
                print(f"Less than {s}. Try again")
            elif s < num:
                print(f"More than {s}. Try again")
            else:
                print("Great!")
                break
        print("Tried 3 times, you've lost.")
        break

def guessing_word():
    words = ['dog', 'cat', 'lel', 'lol2']
    rand_int = random.randint(0, len(words)-1)
    word = words[rand_int]

    while True:
        s = input("Choose a word.\n")

        if s == words[rand_int]:
            print("Great!")
            break
        elif 0 < rand_int < len(words):
            print("Nope!")
            choose = input("Choose (p)revious or (n)ext item.\n Pass 'n' or 'p'").lower()
            if choose == "p":
                rand_int = random.randint(0, rand_int-1)
            else:
                rand_int = random.randint(rand_int-1, len(words)-1)
        words.remove(words[rand_int])
        if len(words) == 0:
            print("You have lost. Quitting")
            break

# read about adv f-strings: https://realpython.com/python-f-strings/

# Ex 2: summing numbers
def mysum(*args):
    total = 0
    for num in args:
        total += num
    return total


def mysum2(num_list, start=0):
    total = start
    for num in num_list:
        total += num
    return total


def myavg(*args):
    total = 0
    for num in args:
        total += num
    return total / len(args)


def words_stats(words):
    words_lenght = []
    for word in words:
        words_lenght.append(len(word))

    return((min(words_lenght), max(words_lenght), sum(words_lenght)/len(words_lenght)))


def sum_numeric_objects(objects):
    total = 0
    for obj in objects:
        try:
            total += int(obj)
        except ValueError:
            pass
    return total


# Ex 3: run timing
def run_timing():
    time_total = 0
    runs = 0

    while True:
        s = input(f"Time for 10 KM in minutes, enter for exit: ")

        if not s:
            break
        else:
            time_total += float(s)
            runs += 1

    if runs > 0:
        print(f"Total time: {time_total} over {runs}. Average of {time_total/runs:.2f}")
    else:
        print("No runs provided.")


def float_splitter(float_no, before=0, after=0):
    float_splitted = str(float_no).split('.')

    print(f"{float_splitted[0][before:]}.{float_splitted[1][:after]}")


# Decimal https://docs.python.org/3.7/library/decimal.html
from decimal import *


def decimal_sum(float_1=0.0, float_2=0.0):
    float_1 = Decimal(str(float_1))
    float_2 = Decimal(str(float_2))

    return sum([float_1, float_2])


# Ex 4 Hexadecimal output
def hex_output():
    dec_num = 0
    hex_num = input("Enter hex number to convert: ")

    for index, hex_digit in enumerate(reversed(hex_num)):  # reverse number, convert to dec, add to sum
        dec_num += int(hex_digit) * 16**index

    return dec_num


def hex_output_2():
    dec_num = 0
    hex_num = input("Enter hex number to convert: ")

    for index, hex_digit in enumerate(reversed(hex_num)):  # reverse number, convert to dec, add to sum
        for i in [ord(chr(x)) for x in range(0, 10)]:
            if str(i) == hex_digit:
                dec_num += ord(chr(i)) * 16 ** index
            else:
                print("Incorrect character detected, quitting")
                break

    return dec_num


def name_triangle(name):
    name_lenght = len(name)

    for i in range(name_lenght+1):
        print(name[:i])

name_triangle("Marian")
