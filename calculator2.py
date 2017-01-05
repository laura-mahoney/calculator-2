"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


# Your code goes here
def is_enough_operands(operands_list, arithmetic_function):
    if len(operands_list) > 1:
        print arithmetic_function
    else:
        print "Please enter enough integers."


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
            is_enough_operands(integers_list, add(integers_list))
        elif operator == "-" or operator == "subtract":
            is_enough_operands(integers_list, subtract(integers_list))
        elif operator == "*" or operator == "multiply":
            is_enough_operands(integers_list, multiply(integers_list))
        
        elif operator == "/" or operator == "divide":
            if len(integers_list) == 2:
                print (divide(integers_list[0], integers_list[1]))
            else:
                print "Please enter two integers."
        elif operator == "power":
            if len(integers_list) == 2:
                print (power(integers_list[0], integers_list[1]))
            else:
                print "Please enter two integers."
        elif operator == "mod":
            if len(integers_list) == 2:
                print (mod(integers_list[0], integers_list[1]))
            else:
                print "Please enter two integers."

        elif operator == "square":
            if len(integers_list) == 1:
                print (square(integers_list[0]))
            else:
                print "Please enter a single integer."
        elif operator == "cube":
            if len(integers_list) == 1:
                print (cube(integers_list[0]))
            else:
                print "Please enter a single integer."
        else:
            print "Please enter valid operator."
