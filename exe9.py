# -*- coding: utf-8 -*-
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)


import random

randNum = random.randint(1,9)
condition = True

while condition:
    print(randNum)
    userInput = input("Enter your Guess: ")
    print(type(userInput))

    if int(userInput) == randNum:
        print("You Win, Try again: ")
        print("")
        randNum = random.randint(1,9)
    elif randNum > int(userInput):
        print("The number is higher than your guess: ")
    elif randNum < int(userInput):
        print("The number is lower than your guess: ")
    elif str(serInput) == "Exit":
        print("Closing")
        condition = False
