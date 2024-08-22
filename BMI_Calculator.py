"""Write a program that calculates the Body Mass Index (BMI) for a user.
   The program should:

Ask the user to input their weight in kilograms.
Ask the user to input their height in meters.
Calculate the BMI using the formula: BMI = weight / (height ** 2)
Handle invalid input for both the weight and height.
Handle the scenario where height is zero or negative .
"""

def bmi():
    try:
        weight=float(input("Enter your weight in kilogram : "))
        height=float(input("Enter your height in meters : "))
        if weight>0 and height>0:
            result=weight/(height**2)
            print("BMI = ",result)
        else:
            print("height and weight should be greater than zero")
    except ValueError:
        print("ERROR ENTER VALID NUMBERS")
bmi()