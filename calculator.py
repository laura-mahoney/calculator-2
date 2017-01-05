"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("Input arithmetic function: ")
    token_input = user_input.split(" ")
    if token_input[0] == 'q' or token_input[0] == 'quit':
        break
    # else: 
    