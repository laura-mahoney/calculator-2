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
        try:
            if token_input[0] == "+" or token_input[0] == "add":
                print add(int(token_input[1]), int(token_input[2]))
            if token_input[0] == "-" or token_input[0] == "subtract":
                print subtract(int(token_input[1]), int(token_input[2]))
            if token_input[0] == "*" or token_input[0] == "multiply":
                print multiply(int(token_input[1]), int(token_input[2]))
            if token_input[0] == "/" or token_input[0] == "divide":
                print divide(int(token_input[1]), int(token_input[2]))
            if token_input[0] == "square":
                print square(int(token_input[1]))
            if token_input[0] == "cube":
                print cube(int(token_input[1]))
            if token_input[0] == "pow":
                print power(int(token_input[1]), int(token_input[2]))
            if token_input[0] == "mod":
                print mod(int(token_input[1]), int(token_input[2]))
        except:
            print "Please enter valid integer."
