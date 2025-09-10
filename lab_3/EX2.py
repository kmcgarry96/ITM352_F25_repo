# create a function called midpoint that takes two numbers as input 
# and returns the value halfway between them.
# Name: Kyle McGarry
# Date: 9/10/2025

def midpoint(num1, num2):
    mid = (num1 + num2) / 2
    return mid


number1= float(input("Enter first number: "))

number2= float(input("Enter second number: "))

result = midpoint(number1, number2)
print(f"the midpoint between {number1} and {number2} is {result}")