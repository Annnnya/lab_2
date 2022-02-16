"""
twitter json navigation
"""

import json
from sys import exit as ex
from random import choice as choic
from pprint import pprint

def we_came_to_the_list(data):
    """
    A part of the program responsible for interactive navigation through list
    """
    print("You navigation journey led you to list!")
    choice = input("Do you want to see the whole list? y/n ")
    if choice == 'exit' or choice == 'quit':
        print('Thank you for choosing our program! Bye!')
        ex()
    elif choice == 'back':
        return 'back'
    elif choice == 'y':
        for num, i in enumerate(data):
            print(num, ')', sep='')
            pprint(i)
    elif choice == 'n':
        choice1 = input(f"Please enter the number of an element you want to see\n \
(the amounts of elements is {len(data)}) ")
        try:
            choice1 = int(choice1)
            if 0 <= choice1 <= len(data)-1:
                pprint(data[choice1])
                choice2 = input("Do you want to take the navigation journey to this level? y/n ")
                if choice2 == 'y':
                    return choice1
                elif choice2 == 'n':
                    print('Then you remain here')
                else:
                    print('Your answer was strange, so we did nothing :^)')
            else:
                print("why do you think I showed you the list's length?\n\
see ya next time :^)")
        except ValueError:
            print('"number" must be the number, silly :^)')
    else:
        print("Please enter a valid responce next time :^)")

def we_came_to_dict(data):
    """
    A part of the program responsible for interactive navigation through dictionary
    """
    print("You navigation journey led you to dictionary!")
    choice = input("Do you want to see the keys? y/n ")
    if choice == 'exit' or choice == 'quit':
        print('Thank you for choosing our program! Bye!')
        ex()
    elif choice == 'back':
        return 'back'
    elif choice == 'y':
        key_list = list(data.keys())
        for num, i in enumerate(key_list):
            print(num, ') ', i)
        choice0 = input("Do you want to see navigate to one of those keys? y/n ")
        if choice0 == 'y':
            number = input("input the number of the key you want to go to ")
            try:
                number = int(number)
                if 0 <= number <= len(data)-1:
                    return key_list[number]
                else:
                    print("why do you think I enumerated the keys?\n\
    see ya next time :^)")
            except ValueError:
                print('"number" must be the number, silly :^)')
        elif choice0 == 'n':
            print('Then you remain here')
        else:
            print('Your answer was strange, so we did nothing :^)')
    elif choice == 'n':
        choice1 = input("Do you want to see the whole dictionary then? y/n ")
        if choice1 == 'y':
            pprint(data)
        elif choice1 == 'n':
            print('Saved us some work. You remain here then)')
        else:
            print('Your answer was strange, so we did nothing :^)')
    else:
        print("Please enter a valid responce next time :^)")

def recursive_journey(dat, val=-1):
    """
    recursive navigation through json
    """
    while True:
        if val != -1:
            data = dat[val]
        else:
            data = dat
        if isinstance(data, list):
            responce = we_came_to_the_list(data)
            if responce is None:
                recursive_journey(data, -1)
            elif responce == 'back':
                return None
            else:
                recursive_journey(data, responce)
        elif isinstance(data, dict):
            responce = we_came_to_dict(data)
            if responce is None:
                recursive_journey(data, -1)
            elif responce == 'back':
                return None
            else:
                recursive_journey(data, responce)
        else:
            print(data)
            print('You are at the lowest level of your navigation journey')
            choice = input('Do you want to quit? y/n ')
            if choice == 'y':
                print('Thank you for choosing our program! Bye!')
                ex()
            elif choice == 'n':
                print('Ok, we took you back')
                recursive_journey(dat, -1)
            else:
                print('Your responce was incomprehensible, so we\
    decided to kick you out! Bye!')
                ex()

def main():
    """
    Reads file and calls interactive function
    """
    path = input("  Hi there!\n\
 You came across interactive navigator through json file!\n\
 If you want to use it, please enter your path to your file:\n\
")
    print()
    print("By the way, at the beginning \
of every new level you can write exit or quit to end the program\n\
or back to go on a higher level\n")
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            recursive_journey(data)
    except FileNotFoundError:
        try:
            random_file = choic(['./twitter1.json', './twitter2.json'])
            with open(random_file, 'r', encoding='utf-8') as file:
                print(f'You entered the path wrong, but we found a "{random_file}" \
at your computer, so don\'t worry! :^)')
                data = json.load(file)
                recursive_journey(data)
        except FileNotFoundError:
            print("The program won't work if you enter invalid path. Bye!")

if __name__=='__main__':
    main()
