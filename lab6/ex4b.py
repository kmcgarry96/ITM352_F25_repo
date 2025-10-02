# Building off ex4.py - Creating isLeapYear function
# name: kyle McGarry 
# date : 10/01/2025

def isLeapYear(year):
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not a leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not a leap year"

# Test it like ex4.py
year = int(input("Enter a year: "))
print(isLeapYear(year))
