# results.py

def show_result(score, total_questions, pass_mark):
    print(f"\nYour final score is: {score}/{total_questions}")
    if score >= pass_mark:
        print("Congratulations! You passed the quiz.")
    else:
        print("You failed the quiz. Better luck next time.")
