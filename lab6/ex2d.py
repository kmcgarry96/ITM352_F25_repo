# Test cases for list length conditions - Building on ex2.py
# name: kyle McGarry 
# date : 10/01/2025

# Original code from ex2.py
ListsOfLists = [[], [1], [2], [3]*12]
print(ListsOfLists)

# Test cases for each condition
test_cases = [
    [],                    # short list (0 elements)
    [1, 2, 3],            # short list (3 elements)
    [1, 2, 3, 4, 5, 6],   # medium list (6 elements)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # medium list (10 elements)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # long list (12 elements)
]

# Test each case using the same logic from ex2.py
for i, test_list in enumerate(test_cases):
    listLength = len(test_list)
    if listLength < 5:
        result = 'short list'
    elif 5 <= listLength <= 10:
        result = 'medium list'
    else:
        result = 'long list'
    
    print(f"Test {i+1}: Length {listLength} -> {result}")

# Original interactive part from ex2.py
print("\nOriginal ex2.py functionality:")
ListNumber = int(input("Enter a list index (0-3): "))
listLength = len(ListsOfLists[ListNumber])
if listLength < 5:
    print('short list')
elif 5 <= listLength <= 10:
    print('medium list')
else:
    print('long list')
