# -*- coding: utf-8 -*-
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)


import random

randNum = random.randint(1,9)
condition = True
numOfGuesses = 0

while True:
    print(randNum)
    userInput = input("Enter your Guess: ")
    numOfGuesses =+1
    print(type(userInput))

    if str(userInput) == "Exit":
        print("Ending: ")
        break
    elif int(userInput) == randNum:
        print("You won in: " + str(numOfGuesses) + " guess, please Try again: ")
        print("")
        randNum = random.randint(1,9)
        numOfGuesses = 0
    elif randNum > int(userInput):
        print("The number is higher than your guess: ")
    elif randNum < int(userInput):
        print("The number is lower than your guess: ")
