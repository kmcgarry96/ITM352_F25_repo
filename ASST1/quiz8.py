#randomize questions and answers. 

# IMPORT FROM THE JSON FILE, DELTE THE QUESTIONS DICTIONARY.
with open("questions.json") as f:
    QUESTIONS = json.load(f)

import random
from string import ascii_lowercase

from string import ascii_lowercase
import random
import json

from quiz2 import QUESTIONS}

num = 0
num_correct = 0
num_questions_per_quiz = 5
num_questions = min(num_questions_per_quiz, len(QUESTIONS))
# randomly select a subject of questions for the quiz.
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"\n{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

for num, (question, alternatives) in enumerate(questions, 1):
    correct_answer = alternatives[0]
    shuffled_alternatives = alternatives.copy()
    random.shuffle(shuffled_alternatives)
    labeled_alternatives = dict(zip(ascii_lowercase, shuffled_alternatives))

    print(f"\nQuestion {num}: {question}")
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    # loop until the user provides a valid answer.
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f'please answer one of {", ".join(labeled_alternatives)}')
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} out of {num} correct ({num_correct/num_questions:.0%})")