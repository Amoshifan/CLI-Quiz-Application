# main.py

import random
from questions import load_questions
from quiz import ask_question, calculate_score
from results import show_result

def main():
    total_questions = 25  # Total number of questions
    pass_mark = 15        # Set the pass mark to 15

    questions = load_questions()

    if len(questions) < total_questions:
        print("Not enough questions available.")
        return

    # Shuffle and select the first 25 questions
    random.shuffle(questions)
    selected_questions = questions[:total_questions]
    
    user_answers = []
    
    for question_data in selected_questions:
        user_answer = ask_question(question_data)
        user_answers.append(user_answer)
    
    score = calculate_score(selected_questions, user_answers)
    show_result(score, len(selected_questions), pass_mark)

if __name__ == "__main__":
    main()
