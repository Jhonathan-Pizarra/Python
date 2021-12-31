'''
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
'''

import re
#your code goes here
num = str(input())
pattern = "\A(1|8|9)\d{7}$"


if re.match(pattern,num):
    print("Valid")
else:
    print("Invalid")
