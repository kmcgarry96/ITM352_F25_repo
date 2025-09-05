# ask the user to enter a floating point number between 1 and 100
# square the number and return the value to the user, rounded to 2 decimal places
# Name: Kyle McGarry
# Date: 9/3/25

value_entered = input("plese enter a floating point number between 1 and 100: ")

value_entered_float = float(value_entered)
squared_value = value_entered_float ** 2
rounded_value = round(squared_value, 2)

print(f"The squared value rounded to 2 decimal places is: {rounded_value}")

                      
        