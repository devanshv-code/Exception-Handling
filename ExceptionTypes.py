input2=input("Enter the number : ")
list1=[1,2,3]
try:
    print(int(input2)*2)
    print(list1[int(input2)])
except ValueError:
    print("the input is not correct ")
except IndexError:
    print("Index error")



try:
    input1=int(input("Enter the number : "))
    input2=int(input("Enter the number : "))
    result=input1/input2
    print(result)
except ZeroDivisionError:
    print("divide by zero is not defined")
except ValueError:
    print("invalid input")
except NameError:
    print(" variable  not found ")


try:
    input1 = int(input("Enter the number : "))
    input2 = int(input("Enter the number : "))
    result = input1/input2
    print(result)
except (ZeroDivisionError,ValueError,NameError) as e:
    print(e)


try:
    input1 = int(input("Enter the number : "))
    input2 = int(input("Enter the number : "))
    result = input1/input2
    print(result)
except (ZeroDivisionError,ValueError,NameError):
    print("error")



import sys
try:
    input1 = int(input("Enter the number : "))
    input2 = int(input("Enter the number : "))
    result = input1/input2
    print(result)
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])