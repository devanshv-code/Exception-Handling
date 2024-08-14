"""
Write a program that defines a list of 5 elements.
Ask the user to enter an index to access an element from the list.
Use exception handling to manage cases where the user enters an index that
is out of range and print an appropriate error message.
"""

list1=[1,2,3,4,5]
input1=int(input("Enter the index to access element : "))
def eh(x):
    try:
        print(list1[x])
    except IndexError:
        print("Index out of range")
eh(input1)