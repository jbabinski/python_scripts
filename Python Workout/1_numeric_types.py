# Ex 1: guessing game
import random

def guessing_game():
    num = random.randint(0, 10)

    while True:
        s = int(input("Provide a number between 1 and 10.\n"))
        if s < num:
            print("More than that.")
        elif s > num:
            print("Less than that.")
        elif s == num:
            print("Correct!")
            break

guessing_game()