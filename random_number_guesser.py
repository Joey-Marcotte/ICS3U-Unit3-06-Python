#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program gets the user to guess a number

import random


def main():

    while True:
        # imput
        integer_as_string = input("pick a number between 0-9:")

        # process
        try:
            integer_as_number = int(integer_as_string)
            if integer_as_number == (random.randint(0, 9+1)):
                # output
                print("You win, you guessed the number")
                break
            else:
                print("wrong, try again")
        except(ValueError):
            print("Not an integer")
        finally:
            print("")


if __name__ == "__main__":
    main()
