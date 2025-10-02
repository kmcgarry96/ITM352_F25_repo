ListsOfLists = [[], [1], [2], [3]*12]
print(ListsOfLists)

ListNumber = int(input("Enter a list index (0-3): "))
listLength = len(ListsOfLists[ListNumber])
if listLength < 5:
    print('short list')
elif 5 <= listLength <= 10:
    print('medium list')
else:
    print('long list')

# this is the ' do it yourself for lab6 exercise, part c

