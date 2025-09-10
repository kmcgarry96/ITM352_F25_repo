# create a module with Handy math functions 
# Name: Kyle McGarry
# Date: 9/10/2025


#function to return the midpoint between two numbers
def midpoint(num1, num2):
    mid = (num1 + num2) / 2
    return mid


number1= float(input("Enter first number: "))

number2= float(input("Enter second number: "))

result = midpoint(number1, number2)
print(f"the midpoint between {number1} and {number2} is {result}")

#function to return the square root of a number

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    return x ** 0.5

number = float(input("Enter a number: "))
result = square_root(number)
print(f"The square root of {number} is {result}")   


# funcion to return the result of raising base to the exponent exp
def power(base, exp):
    return base ** exp



# function to return the maximum of two numbers

def max(a,b):
    
    return a if a > b else b

# function to return the minimum of two numbers
def min(a, b):
    return a if a < b else b

