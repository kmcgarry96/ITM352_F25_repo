# manipulate a list in various ways
# name: kyle McGarry
# date: 9/17/2025

response_values = [5, 7, 3, 8]

response_values.append(0)

print ("after appending 0:", response_values)

# Insert 6 at index 2 using slicing and +
response_values = response_values[:2] + [6] + response_values[2:]
print("after inserting 6 at index 2 with slicing and +:", response_values)

# Explanation:
# The + operator joins lists together, making a new list with all the items.
# For strings, + joins text together (concatenation).
# For numbers, + adds the values together (math addition).

# copilot reccomended this way. did not do this part in class.
