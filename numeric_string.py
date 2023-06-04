# Python program to identify the Digit

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for identifying a digit
regex = '^[0-9]+$'


# Define a function for
# identifying a Digit
def check(string):
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, string)):
        return True
        print("Digit")

    else:
        return False
        print("Not a Digit")

