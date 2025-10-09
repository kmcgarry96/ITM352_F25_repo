# quiz questions. for each questions, give a corresponding number next to each possible answer.
# imporve look and usibility. keep track of corect answers


from string import ascii_lowercase



QUESTIONS = {
    "what is the airspeed of a anladen swallow in miles per hour?": ["12", "24", "36", "48"],
    "what is the capital of texas?": ["austin", "dallas", "houston", "san antonio"],
    "the last supper was painted by which artist?": ["da vinci", "michelangelo", "raphael", "donatello"]
}
num = 0
num_correct = 0
for question, alternatives in enumerate(QUESTIONS.items()):
    print(f"\nQuestion {num}:)")
    print(f"{question}")

    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")


answer_label = int("\nChoice?")
answer = labeled_alternatives.get(answer_label)
if answer == correct_answer:
    print("correct")
    num_correct += 1
else:
    print(f"the answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} out of {num} correct ({num_correct/num:.0%})")