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
    integers_list = []

    try:
        for token in token_input[1:]:
            integers_list.append(int(token))
    except:
        print "Please enter a list with valid integers."
        continue

    if token_input[0] == 'q' or token_input[0] == 'quit':
        break
    else:
        try:
            if token_input[0] == "+" or token_input[0] == "add":
                reduced_output = reduce(lambda a, b: a + b, integers_list[1:])
                print add(integers_list[0], reduced_output)
            elif token_input[0] == "-" or token_input[0] == "subtract":
                reduced_output = reduce(lambda a, b: a - b, integers_list[0:-1])
                print subtract(reduced_output, integers_list[-1])
            elif token_input[0] == "*" or token_input[0] == "multiply":
                reduced_output = reduce(lambda a, b: a * b, integers_list[1:])
                print multiply(integers_list[0], reduced_output)
            elif token_input[0] == "/" or token_input[0] == "divide":
                reduced_output = reduce(lambda a, b: a / b, integers_list[0:-1])
                print divide(reduced_output, integers_list[-1])
            elif token_input[0] == "square":
                print square(integers_list[0])
            elif token_input[0] == "cube":
                print cube(integers_list[0])
            elif token_input[0] == "pow":
                print power(integers_list[0], integers_list[1])
            elif token_input[0] == "mod":
                print mod(integers_list[0], integers_list[1])
            else:
                print "Please enter valid operator."
        except:
            print "Please enter valid integer."
