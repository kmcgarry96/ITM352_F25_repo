#quiz 2 - put answers into a list 

#name: Kyle McGarry 
#date: 10/3/2025

QUESTIONS = [("what is the airspeed of a anladen swallow in miles per hour?", "12"), ("what is the capital of texas?", "austin"), ("the last supper was painted by which artist?", "da vinci")]

for question, correct_answer in QUESTIONS:
    answer = input(question)
    if answer.lower() == correct_answer:
        print("correct")
    else:
        print(f"the answer is {correct_answer!r}, not {answer!r}")

