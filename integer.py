#!/usr/bin/env python3
# Created By: Alex M
# Date: Oct 19, 2023
# This program makes the user guess a number .


def main():
    # get number from user as an integer 
    user_number = int(input(print(" give an integer ")))
    print("")

    #find out if number is positive, negative or 0
    if user_number > 0: 
        print(user_number, " positive integer ")
    elif user_number < 0:
        print(user_number, " negative integer ")
    else:
        print (user_number, " number is 0 ")
    

if __name__ == "__main__":
    main()




