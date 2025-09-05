def Ftoc(degreesF):
    degreesF_Float = float(degreesF)
    degreesC = (degreesF_Float - 32) * 5.0/9.0
    degreesC = round(degreesC, 2)
    return degreesC

degreesF = input (" enter a temperature in degrees Fahrenheit: ")
degreesC = Ftoc(degreesF,1)
print (f"{degreesF} degrees Fahrenheit is {degreesC} degrees Celsius")

