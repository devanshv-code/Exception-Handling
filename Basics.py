input1=input("Enter the number : ")
try:
    print(int(input1)*2)
except:
    print("ERROR")


input1=input("Enter the number : ")
try:
    print(int(input1)*2)
except:
    print("ERROR")
else:
    print("code runs without errors")
finally:
    print("completed")


try:
    input1=input("Enter the  number : ")
    print(int(input1)*2)
except:
    print("invalid input")
else:
    print("code runs without errors")
finally:
    print("finish")