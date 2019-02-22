name = input("Please Enter Your name: ")

age = int(input("Please Enter your age: "))

print("xzcxzcxz")
numOfCopy = int(input("How many times do you want to repeat the message?: "))

newAge = 2019 + (100 - age)

for x in range(0, numOfCopy):
    print("Hi " + name + " You will be 100 years old in " + str(newAge))
