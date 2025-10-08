celebrities_tuple = ("taylor swift", "lionel messi", "max verstappen", "keanu reeves", "angelina jolie")
ages_tuple = (34, 36, 26, 60, 48)
celebrities_list = []
ages_list = []

for celeb in celebrities_tuple:
    celebrities_list.append(celeb)


for age in ages_tuple:
    ages_list.append(age)

celebrities_dictionary = {"celebrities": celebrities_list, "ages": ages_list}

print(celebrities_dictionary)


