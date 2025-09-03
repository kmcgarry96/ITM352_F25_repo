
# ask the user to enter a floating point (decimal number) between 1 and 100. Square the number 
# and print the result.
# Name: Kyle McGarry 
#Date: 9/3/25
# ...existing code...
Value_entered = input("please enter a floating point number between 1 and 100:")
print(" the user entered ", Value_entered)
value_as_float = float (Value_entered)

value_squared = value_as_float**2
print(f" the value squared is {value_squared}")
