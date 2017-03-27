# 01 - Write a function that computes the volume of a sphere given its radius.
import math


def vol(rad):
    return (4.0/3) * math.pi * (rad**3)


# 02 - Write a function that checks whether a number
# is in a given range (Inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print ("%s is in range %s - %s" % (num, low, high))
    else:
        print("%s is out of the range" % (num))


# Bool version
def ran_bool(num, low, high):
    return num in range(low, high + 1)


# 03 - Write a Python function that accepts a string and calculate the
# number of upper case letters and lower case letters.
def up_low(s):
    u = 0
    l = 0
    for string in s:
        if string.islower():
            l += 1
        elif string.isupper():
            u += 1
    print("No. of Upper case characters : %s" % (u))
    print("No. of Lower case characters : %s" % (l))


# 04 - Write a Python function that takes a list and returns a new list with
# unique elements of the first list.
def unique_list(l):
    s = set(l)
    return list(s)


# 05 - Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    mult = 1
    for i in numbers:
        mult *= i
    return mult


# 06 - Write a Python function that checks whether a passed string is
# palindrome or not.
def palindrome(s):
    return s == s[::-1]


# 07 - Hard: Write a Python function to check whether a string is pangram
# or not.
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = set(str1.lower())
    alphabet = set(alphabet)
    return alphabet <= str1
