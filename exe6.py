#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def palindrome(myStr):

    newStr = myStr[::-1].lower()

    print(newStr)
    print(myStr)

    if newStr == myStr.lower():
        return True
    else:
        return False




print(palindrome("Anna"))
# a = "Waleed"
# strLen = len(a)
# b = a[::-1]
# print(b)
