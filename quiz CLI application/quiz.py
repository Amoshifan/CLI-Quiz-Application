# quiz.py

def ask_question(question_data):
    question = question_data["question"]
    options = question_data["options"]
    
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Select an option (1-4): "))
            if 1 <= answer <= 4:
                return options[answer - 1]
        except ValueError:
            print("Invalid input. Please select a number between 1 and 4.")

def calculate_score(questions, user_answers):
    score = 0
    for i, question_data in enumerate(questions):
        if user_answers[i] == question_data["answer"]:
            score += 1
    return score
