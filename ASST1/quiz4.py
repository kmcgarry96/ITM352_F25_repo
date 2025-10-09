# quiz 4. put questons into a dictionary to include answer options.



# quiz questions. for each questions, give a corresponding number next to each possible answer.

QUESTIONS = {
    "what is the airspeed of a anladen swallow in miles per hour?": ["12", "24", "36", "48"],
    "what is the capital of texas?": ["austin", "dallas", "houston", "san antonio"],
    "the last supper was painted by which artist?": ["da vinci", "michelangelo", "raphael", "donatello"]
}

for question, alternatives in QUESTIONS.items():
    
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives, start=1):
        print(f"{label}. {alternative}")

        answer_label = int(input(f"{question}? "))
        if answer_label == 1:
            print("correct")
        else:
            print(f"the answer is {correct_answer!r}, not {alternative!r}")
