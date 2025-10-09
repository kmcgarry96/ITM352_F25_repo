celebrities_tuple = ("taylor swift", "lionel messi", "max verstappen", "keanu reeves", "angelina jolie")
ages_tuple = (34, 36, 26, 60, 48)
celebrities_list = []
ages_list = []

for celeb in celebrities_tuple:
    celebrities_list.append(celeb)


for age in ages_tuple:
    ages_list.append(age)

celebrities_dictionary = {"celebrities": celebrities_list, "ages": ages_list}

print("With loops:")
print(celebrities_dictionary)

# Do the above without loops
celebrities_tuple2 = ("taylor swift", "lionel messi", "max verstappen", "keanu reeves", "angelina jolie")
ages_tuple2 = (34, 36, 26, 60, 48)

celebrities_dictionary2 = {"celebrities": list(celebrities_tuple2), "ages": list(ages_tuple2)}

print("\nWithout loops:")
print(celebrities_dictionary2)


