#    Title: stephens_calculator.py
#    Author: Kailee Stephens
#    Date: 28 August 2022
#    Description: Assignment 3.3 - Python Variables and Functions

# Functions with returns
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def divide (x, y):
    return x / y

def multiply (x, y):
    return x * y

#Variables to test each function
num1 = 4
num2 = 10
num3 = 6
num4 = 8
num5 = 2

#Variable to hold values from above methods
add_total = add(num1, num1)
sub_total = subtract(num2, num3)
div_total = divide(num4, num5)
mul_total = multiply(num2, num5)

#Variable to hold string output
output = "4 + 4 is {0}".format(add_total)
output = "10 - 6 is {0}".format(sub_total)
output = "8 / 2 is {0}".format(div_total)
output = "10 * 2 is {0}".format(mul_total)

print(output)
