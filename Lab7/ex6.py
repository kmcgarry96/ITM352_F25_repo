# Exercise 6: Tuple append with error handling
data = ("hello", 10, "goodbye", 3, "goodnight", 5)
user_input = input("Enter a value to append: ")


# Try to append (will fail)
try:
   data.append(user_input)
except AttributeError:
   print("Can't append to tuple - they're immutable!")
   # Fix it by creating new tuple
   data = data + (user_input,)
   print("New tuple:", data)

    