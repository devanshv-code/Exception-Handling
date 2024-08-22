"""
Write a program that asks the user to input two numbers and then
divides the first number by the second number. Use exception handling to
manage the case where the user inputs zero
as the second number and print an appropriate error  message.
"""

input1=int(input("enter the number : "))
input2=int(input("enter the number : "))
def div(x,y):
    try:
        print(x/y)
    except:
        print("can not divide by zero")
div(input1,input2)



try:
    input1 = int(input("Enter the number : "))
    input2 = int(input("Enter the number : "))
    result = input1/input2
    print(result)
except ZeroDivisionError as e:
    print(e.__class__)
    print(e)