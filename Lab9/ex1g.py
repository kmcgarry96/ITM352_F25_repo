# Add name to the end of names.txt and print all contents

with open('names.txt', 'a') as file_object:
    file_object.write("kyle mcgarry\n")

print("Contents of names.txt:")
with open('names.txt', 'r') as file_object:
    while True:
        line = file_object.readline()
        if not line:
            break
        print(line.strip())
