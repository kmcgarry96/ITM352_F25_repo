data = ("hello", 10, "goodbye", 3, "goodnight", 5)
string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1
        print(f"there are {string_count} strings in the tuple")
        