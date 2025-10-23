with open('names.txt', 'r') as file_object:
    while True:
        line = file_object.readline()
        if not line:
            break
        print(line.strip())

