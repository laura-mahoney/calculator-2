"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


# Your code goes here
while True:
    user_input = raw_input("Input arithmetic function: ")
    token_input = user_input.split(" ")
    operator = token_input[0]
    integers_list = []

    try:
        for token in token_input[1:]:
            integers_list.append(int(token))
    except:
        print "Please enter a list with valid integers."
        continue

    if operator == 'q' or operator == 'quit':
        break
    else:
        if operator == "+" or operator == "add":
            print add(integers_list)
        elif operator == "-" or operator == "subtract":
            print subtract(integers_list)
        elif operator == "*" or operator == "multiply":
            print multiply(integers_list)
        elif operator == "/" or operator == "divide":
            print divide(integers_list[0], integers_list[1])
        elif operator == "square":
            print square(integers_list[0])
        elif operator == "cube":
            print cube(integers_list[0])
        elif operator == "pow":
            print power(integers_list[0], integers_list[1])
        elif operator == "mod":
            print mod(integers_list[0], integers_list[1])
        else:
            print "Please enter valid operator."
