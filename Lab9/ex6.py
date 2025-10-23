# read a file of questions from a json file and save them 
# in a dictionary. print the dictionary to the console.
import json

#specify the file name 
JSON_File = 'quiz_questions.json'

with open(JSON_File, 'r') as json_file:
    data = json.load(json_file)

print(data)

