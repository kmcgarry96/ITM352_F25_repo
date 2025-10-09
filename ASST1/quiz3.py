
# quiz 3. put questons into a dictionary to include answer options.



# quiz questions. for each questions, list the possible answers with the first being the correct one.

QUESTIONS = {
    "what is the airspeed of a anladen swallow in miles per hour?": ["12", "24", "36", "48"],
    "what is the capital of texas?": ["austin", "dallas", "houston", "san antonio"],
    "the last supper was painted by which artist?": ["da vinci", "michelangelo", "raphael", "donatello"]
}

for question, alternatives in QUESTIONS.items():
    
    correct_answer = alternatives[0]
    for alernative in sorted(alternatives):
        print(f" - {alernative}")

    answer = input(question)
    if answer.lower() == correct_answer:
        print("correct")

    else:
        print(f"the answer is {correct_answer!r}, not {answer!r}")


    