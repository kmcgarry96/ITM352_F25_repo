# ask the user to enter thier weight in pounds. Convert the value to kilograms and return the value to the user, rounded to 2 decimal places.
# Name: Kyle McGarry
# Date: 9/3/25


weight_in_pounds = input("please enter your weight in pounds: ")
weight_in_kilos = round(float(weight_in_pounds) * 0.453592, 2)
weight_in_kilos_rounded = round(weight_in_kilos, 2)
print(f"your weight in kilograms is: {weight_in_kilos_rounded} kg")
