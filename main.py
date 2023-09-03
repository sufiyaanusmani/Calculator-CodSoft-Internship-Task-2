# Author: Sufiyaan Usmani
# Email: usmanisufiyaan@gmail.com
# CodSoft Internship Task 2

import os

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Using High Order Function
def calculate(num1, num2, operation):
    return operation(num1, num2)

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    os.system('cls')
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        op = input('Enter operator: ')

        # if invalid operator is entered
        if op not in operators.keys():
            print('Invalid operator!')
            continue
        result = calculate(num1, num2, operators[op])
    except Exception as e:
        print(e)
    else:
        print(result)
        choice = input('Do you want to continue [y/n]: ')
        if 'n' in choice.lower():
            break

