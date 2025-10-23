with open('names.txt', 'r') as file_object:
    contents = file_object.read()
    print(contents)
# also print the amount of names in the file
    names = contents.splitlines()
    print(f'The file contains {len(names)} names.')
    print(names)
    