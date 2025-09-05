# ask the user for their birth year. Calculate their age by subtracting from the current year.
# Name: Kyle McGarry
# date: 9/3/25

birth_year = input (" please enter your birth year as a four digit number: ")
birth_year_int = int(birth_year)


# this should be changed to extract the year automaticly from the current date.
current_year = 2025

# this doesnt take into account the day and month. need to fix.
age = current_year - birth_year_int
print ("you entered", birth_year)
print ("your age is ", age)
