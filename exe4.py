# -*- coding: utf-8 -*-
## # Create a program that asks the user for a number and then prints out a
# list of all the divisors #of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into #another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)


def divisors(x):
    numbers = range(x,0,-1)
    divisorList = []

    for y in numbers:
<<<<<<< HEAD
        if (x%y == 0):
            return y





print(divisors(10))
=======
        if(x%y == 0):
            divisorList.append(y)
>>>>>>> 4aadb0e984bad04bcd40537c92cc972bb17ccf7e

    #divisorList.reverse()
    return divisorList

<<<<<<< HEAD
# x = 10
# numbers = range(x,0,-1)
#
# for x in numbers:
#     if(10%x == 0):
#         print(x)
=======

print(divisors(10))
>>>>>>> 4aadb0e984bad04bcd40537c92cc972bb17ccf7e
