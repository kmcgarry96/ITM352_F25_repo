# Exercise 6 Parts c, d, e, f
data = ("hello", 10, "goodbye", 3, "goodnight", 5)
user_input = input("Enter a value to append: ")

# (c) Report error with exception details
try:
    data.append(user_input)
except AttributeError as e:
    print(f"Attempted to append to tuple. Error: {e}")

# (d) Handle by creating new tuple with +
data = ("hello", 10, "goodbye", 3, "goodnight", 5)  # Reset
try:
    data.append(user_input)
except AttributeError:
    data = data + (user_input,)
    print("New tuple:", data)

# (e) Use unpacking operator *
data = ("hello", 10, "goodbye", 3, "goodnight", 5)  # Reset
try:
    data.append(user_input)
except AttributeError:
    data = (*data, user_input)
    print("Unpacked tuple:", data)

# (f) Convert to list, append, convert back
data = ("hello", 10, "goodbye", 3, "goodnight", 5)  # Reset
data_list = list(data)
data_list.append(user_input)
data = tuple(data_list)
print("Final tuple:", data)
