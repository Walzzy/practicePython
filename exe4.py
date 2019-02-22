# -*- coding: utf-8 -*-
## # Create a program that asks the user for a number and then prints out a
# list of all the divisors #of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into #another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)


def divisors(x):
    numbers = range(x,0,-1)
    divisorList = []

    for y in numbers:
        if(x%y == 0):
            divisorList.append(y)

    #divisorList.reverse()
    return divisorList


print(divisors(10))
