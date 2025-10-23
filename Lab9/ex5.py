# save the dictionary of quiz questions toa. json file
import json

questions = {
    "who was the first president of the united states?": ["george washington", "john adams", "thomas jefferson", "benjamin franklin"],
    "in what year did world war ii end?": ["1945", "1944", "1946", "1943"],
    "which ancient wonder of the world was located in egypt?": ["great pyramid of giza", "hanging gardens", "colossus of rhodes", "lighthouse of alexandria"],
    "who was the first person to walk on the moon?": ["neil armstrong", "buzz aldrin", "john glenn", "alan shepard"],
    "what year did the titanic sink?": ["1912", "1910", "1914", "1911"]
}

JSON_file = "quiz_questions.json"

with open(JSON_file, 'w') as json_file:
    json.dump(questions, json_file)

    print(f"Quiz questions saved to {JSON_file}")

    