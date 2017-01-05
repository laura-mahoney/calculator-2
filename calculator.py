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
    else:
        if token_input[0] == "+":
            add(token_input[1], token_input[2])
        if token_input[0] == "-":
            subtract(token_input[1], token_input[2])
        if token_input[0] == "*":
            multiply(token_input[1], token_input[2])
        if token_input[0] == "/":
            divide(token_input[1], token_input[2])
        if token_input[0] == "square":
            square(token_input[1])
        if token_input[0] == "cube":
            cube(token_input[1])
        if token_input[0] == "pow":
            power(token_input[1], token_input[2])
        if token_input[0] == "mod":
            mod(token_input[1], token_input[2])
