
# Assignment 1: Quiz Application
# Interactive multiple-choice quiz with speed bonuses and high score tracking
# EXTRA CREDIT: Multi-user system with individual high scores and grand champion tracking

# name: Kyle McGarry 
# due 10/14/25


# AI USAGE DOCUMENTATION:
#
# AI Tool Used: GitHub Copilot
#
# Specific AI Assistance:
# - Prompt: "Help me implement a user login system with JSON file storage"
#   AI provided: Basic structure for load_user_data() and save_user_data() functions
#   My contribution: Modified to include grand champion tracking and games played counter
#
# - Prompt: "Add speed bonuses for fast quiz answers"  
#   AI provided: Timer logic using time.time() 
#   My contribution: Set 10-second threshold, added emoji feedback, integrated with scoring
#
# - Prompt: "Help me consolidate and clean up my code"
#   AI provided: Suggestions to remove unused functions
#   My contribution: Decided which functions to keep, maintained code organization
#
# Student Work (No AI):
# - All 5 history questions were written by me
# - Quiz topic selection (history theme)
# - Variable naming conventions
# - Testing and debugging
# - Overall program design decisions

# Import required libraries for randomization, timing, JSON file handling, and alphabet letters
import random
import time
import json
from string import ascii_lowercase

def load_user_data():
    """Load all user data from file. Returns empty dict if file doesn't exist."""
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": {}, "grand_champion": {"name": "", "score": 0}}

def save_user_data(user_data):
    """Save all user data to file."""
    with open('users.json', 'w') as f:
        json.dump(user_data, f, indent=2)

def login_user():
    """Get username from user and return user info. Creates new user if needed."""
    username = input("\nEnter your username: ").strip().lower()
    if not username:
        username = "guest"
    
    user_data = load_user_data()
    
    # Create new user if doesn't exist
    if username not in user_data["users"]:
        user_data["users"][username] = {"high_score": 0, "games_played": 0}
        save_user_data(user_data)
        print(f"Welcome new player, {username.title()}!")
    else:
        user_info = user_data["users"][username]
        print(f"Welcome back, {username.title()}!")
        print(f"Your high score: {user_info['high_score']} | Games played: {user_info['games_played']}")
    
    return username, user_data

def run_quiz():
    """Main quiz function that handles the entire quiz flow including timing, scoring, and user-specific high score tracking."""
    # EXTRA CREDIT: User login and personalized scoring system
    # Each user gets their own high score tracking and contributes to grand champion competition
    username, user_data = login_user()
    current_user = user_data["users"][username]
    
    # Load quiz questions from external JSON file
    with open('questions.json', 'r') as f:
        QUESTIONS = json.load(f)

    # Initialize quiz tracking variables (scores start at 0, quiz has 5 questions)
    num_correct = bonus_points = 0
    num_questions = 5
    # Randomly select questions from the question bank
    questions = random.sample(list(QUESTIONS.items()), k=min(num_questions, len(QUESTIONS)))

    # Start timing the entire quiz
    start_time = time.time()

    # Main quiz loop - present each question and process answers
    for num, (question, alternatives) in enumerate(questions, 1):
        # First answer in list is always correct, others are shuffled for display
        correct_answer = alternatives[0]
        shuffled_alternatives = alternatives.copy()
        random.shuffle(shuffled_alternatives)
        # Map answers to letters (a, b, c, d)
        labeled_alternatives = dict(zip(ascii_lowercase, shuffled_alternatives))

        # Display the question and answer choices
        print(f"\nQuestion {num}: {question}")
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        # Time how long user takes to answer this question
        question_start_time = time.time()
        # Keep asking until user enters a valid choice (a, b, c, or d)
        while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
            print(f'please answer one of {", ".join(labeled_alternatives)}')
        
        question_time = time.time() - question_start_time
        answer = labeled_alternatives.get(answer_label)
        
        # Evaluate answer and award points (including speed bonus for fast correct answers)
        if answer == correct_answer:
            print("Correct!")
            num_correct += 1
            if question_time < 10.0:  # Award bonus point for answers under 10 seconds
                bonus_points += 1
                print(f"⚡ SPEED BONUS! Answered in {question_time:.1f} seconds (+1 bonus point)")
            else:
                print(f"Answered in {question_time:.1f} seconds")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
            print(f"Answered in {question_time:.1f} seconds")

    # Calculate final results and display comprehensive score breakdown
    total_time = time.time() - start_time
    final_score = num_correct + bonus_points  # Total score includes speed bonuses

    print(f"\nQUIZ RESULTS:")
    print(f"Correct answers: {num_correct} out of {num}")
    print(f"Speed bonus points: {bonus_points}")
    print(f"Final score: {final_score} ({num_correct/num_questions:.0%} accuracy)")
    print(f"Total time: {total_time:.2f} seconds")

    # Update user statistics
    current_user["games_played"] += 1
    user_high_score = current_user["high_score"]
    
    # Check for personal high score
    if final_score > user_high_score:
        print(f"\n🎉 PERSONAL HIGH SCORE! 🎉")
        print(f"Previous personal best: {user_high_score}")
        print(f"Your new personal best: {final_score}")
        current_user["high_score"] = final_score
        
        # Check for grand champion
        grand_champ = user_data["grand_champion"]
        if final_score > grand_champ["score"]:
            print(f"\n👑 NEW GRAND CHAMPION! 👑")
            print(f"Previous grand champion: {grand_champ['name'].title()} ({grand_champ['score']})")
            print(f"You are now the GRAND CHAMPION with {final_score} points!")
            user_data["grand_champion"] = {"name": username, "score": final_score}
        
        save_user_data(user_data)
    else:
        print(f"\nYour personal best: {user_high_score}")
        grand_champ = user_data["grand_champion"]
        if grand_champ["name"]:
            print(f"Grand Champion: {grand_champ['name'].title()} ({grand_champ['score']} points)")
        
        # Still need to update games played
        save_user_data(user_data)


# Run the quiz when the script is executed
if __name__ == "__main__":
    run_quiz()