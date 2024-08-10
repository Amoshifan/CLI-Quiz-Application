# quiz.py

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()
    return answer

def calculate_score(questions, user_answers):
    score = 0
    for i, question in enumerate(questions):
        if question["answer"] == user_answers[i]:
            score += 1
    return score
