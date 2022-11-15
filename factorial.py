#!/usr/bin/env python3

# Created By: Jessah
# Date: Nov 15, 2022
# This program ask the user for a positive integer and it will track the loop.
# and it will produce the factorial of said number


def main():
    # declare variables
    counter = 0
    factorial = 1
    # get input from user
    user_string = input("Enter a positive number: ")
    # try catch any strings or floats
    try:
        user_int = int(user_string)
    except Exception:
        print("")
        print("{} is invalid,".format(user_string))
        print("Enter a positive number")
    else:
        if user_int >= 0:  # catch any negative numbers
            while True:
                counter = counter + 1
                factorial = factorial * counter
                print("Tracking {} in the loop".format(counter))
                if counter >= user_int:
                    break
            print("")
            # display the factorial of the user input
            print("The product of {}! is {}".format(user_int, factorial))
            print("{}! = {}".format(user_int, factorial))
        else:  # display when negative number
            print("")
            print("{} is a negative number".format(user_int))
            print("Enter a positive number")


if __name__ == "__main__":
    main()
