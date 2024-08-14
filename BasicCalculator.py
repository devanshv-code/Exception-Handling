"""
Simple Calculator with Exception Handling
Description: Write a program that acts as a simple calculator. The program should:

Ask the user to input two numbers.
Ask the user to select an operation to perform
(addition, subtraction, multiplication, division).
Handle invalid input for both the numbers and the chosen operation.
Handle division by zero.
Handle any other unexpected errors gracefully.
Operations:

+ for Addition
- for Subtraction
* for Multiplication
/ for Division
"""

import sys
try:
    no1=float(input("Enter the first number : "))
except ValueError:
    print("Invalid first input")
    sys.exit()

try:
    op=str(input("Enter the operator [+,-,*,/]"))
    list1=['-','+','*','/']
    index1=list1.index(op)
except:
    print("Invalid operator")
    sys.exit()

try:
    no2=int(input("Enter the second number : "))
except:
    print("Invalid second input")
    sys.exit()

try:
    def addition(x,y):
        return(x+y)
    def sub(x,y):
        return(x-y)
    def mul(x,y):
        return(x*y)
    def div(x,y):
        return(x/y)
    if op=="+":
        print(addition(no1,no2))
    elif op=="-":
        print(sub(no1,no2))
    elif op=="*":
        print(mul(no1,no2))
    else:
        print(div(no1,no2))
except ZeroDivisionError:
    print("CANNOT DIVIDE BY ZERO")