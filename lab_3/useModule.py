# test to see how th function defined in HandyMath work.
# name: Kyle McGarry
# date: 9/10/2025

import HandyMath as hm
from HandyMath import max, min 


number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))

mid = hm.midpoint(number1, number2)
print(f" the midpoint between {number1} and {number2} is {mid}")

exp = hm.exponent(number1, number2)
print(f"{number1} raised to the power of {number2} is {exp}")


max_number = hm.max(number1, number2)
print(f"The maximum of {number1} and {number2} is {max_number}")

min_number = hm.min(number1, number2)
print(f"The minimum of {number1} and {number2} is {min_number}")

sq_root = hm.square_root(number1)
# using abs to avoid value error
print(f"The square root of {abs(number1)} is {sq_root}")
