# create a new dictionary


country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"}

# print the dictionary
print(country_capitals) 

country_capitals["Italy"] = "Rome"

print(country_capitals)

del country_capitals["Japan"]



country_capitals["Italy"] = "Milan"

print(country_capitals)


print(len(country_capitals))

print("India" in country_capitals)

print("canada" not in country_capitals)

