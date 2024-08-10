# main.py

import random
from questions import load_questions
from quiz import ask_question, calculate_score
from results import show_result

def main():
    pass_mark = 2  # Pass mark is set to 2 out of 3 questions
    questions = load_questions()

    # Shuffle the questions randomly
    random.shuffle(questions)
    
    user_answers = []
    
    for question_data in questions:
        user_answer = ask_question(question_data)
        user_answers.append(user_answer)
    
    score = calculate_score(questions, user_answers)
    show_result(score, len(questions), pass_mark)

if __name__ == "__main__":
    main()
