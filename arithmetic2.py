def add(num_list):
    """Return the sum of a list of numbers"""
    total = 0
    for num in num_list:
        total += num
    return total

def subtract(num_list):
    """Return the difference of a list of numbers"""
    difference = num_list[0]
    for num in num_list[1:]:
        difference -= num
    return difference

def multiply(num_list):
    """Return the product of a list of numbers"""
    total = 1
    for num in num_list:
        total *= num
    return total

def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / float(num2)

def square(num):
    """Return the square of a number"""
    return num * num

def cube(num):
    """Return the cube of a number"""
    return num ** 3

def power(num, exponent):
    """Return num raised to the power of exponent"""
    return num**exponent

def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
