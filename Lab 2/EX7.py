# ask the user to enter a temperature in degrees Fahrenheit. Convert the value to degrees Celsius and return the value to the user, rounded to 2 decimal places.
# Name: Kyle McGarry
# Date: 9/3/25








degreesF = input (" enter a temperature in degrees Fahrenheit: ")

degreesF_Float = float(degreesF)
degreesC = (degreesF_Float - 32) * 5.0/9.0

print (f"{degreesF_Float} degrees Fahrenheit is {round(degreesC, 2)} degrees Celsius")
