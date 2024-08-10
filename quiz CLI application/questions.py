# questions.py

def load_questions():
    questions = [
        {
            "question 1": "Which type of Programming does Python support?",
            "options": ["A) object-oriented programming", "B) structured programming", "C) functional programming", "D) all of the mentioned"],
            "answer": "D"
        },
        {
            "question 2": "Is Python case sensitive when dealing with identifiers?",
            "options": ["A) No", "B) Yes", "C) Machine dependent", "D) None of the mentioned"],
            "answer": "B"
        },
        {
            "question 3": "Which of the following is the correct extension of the Python file'?",
            "options": ["A) .python", "B) .pl", "C) .py", "D) .p"],
            "answer": "C"
        },
        {
            "question 4": "Is Python code compiled or interpreted'?",
            "options": ["A) Python code is both compiled and interpreted", "B) Python code is neither compiled nor interpreted", "C) Python code is only compiled", "D) Python code is only interpreted"],
            "answer": "D"
        },
        {
            "question 5": "All keywords in Python are in _____'?",
            "options": ["A) Capitalized", "B) lower case", "C) UPPER CASE", "D) None of the mentioned"],
            "answer": "B"
        },
        {
            "question 6": "What will be the value of the following Python expression? 4 + 3 % 5'",
            "options": ["A) 7", "B) 2", "C) 4", "D) 1"],
            "answer": "A"
        },
        {
            "question 7": "Which of the following is used to define a block of code in Python language'?",
            "options": ["A) Indentation", "B) Key", "C) Brackets", "D) All of the mentioned"],
            "answer": "A"
        },
        {
            "question 8": "Which keyword is used for function in Python language'?",
            "options": ["A) Function", "B) def", "C) Fun", "D) Define"],
            "answer": "B"
        },
        {
            "question 9": "Which of the following character is used to give single-line comments in Python'?",
            "options": ["A) //", "B) #", "C) !", "D) /*"],
            "answer": "B"
        },
        {
            "question 10": "Which of the following functions can help us to find the version of python that we are currently working on'?",
            "options": ["A) sys.version(1)", "B) sys.version(0)", "C) sys.version()", "D) sys.version"],
            "answer": "C"
        },
        {
            "question 11": "Python supports the creation of anonymous functions at runtime, using a construct called ____'?",
            "options": ["A) pi", "B) anonymous", "C) lambda", "D) none of the mentioned"],
            "answer": "C"
        },
        {
            "question 12": "What is the order of precedence in python'?",
            "options": ["A) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "B) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction", "C) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition", "D) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
            "answer": "A"
        },
        {
            "question 13": "What does pip stand for python'?",
            "options": ["A) Pip Installs Python", "B) Pip Installs Packages", "C) Preferred Installer Program", "D) All of the mentioned"],
            "answer": "C"
        },
        {
            "question 14": "Which of the following is true for variable names in Python'?",
            "options": ["A) underscore and ampersand are the only two special characters allowed", "B) unlimited length", "C) all private members must have leading and trailing underscores", "D) none of the mentioned"],
            "answer": "B"
        },
        {
            "question 15": "What are the values of the following Python expressions' \n 2(32) \n 2(32) \n (23)2 \n 232 ?",
            "options": ["A) 512, 64, 512", "B) 512, 512, 512", "C) 64, 512, 64", "D) 64, 64, 64"],
            "answer": "A"
        },
        {
            "question 16": "Which of the following is the truncation division operator in Python'?",
            "options": ["A) |", "B) //", "C)  /", "D)  %"],
            "answer": "B"
        },

        {
            "question 17": "What will be the output of the following Python code' l=[1, 0, 2, 0, 'hello', '', []] \n list(filter(bool, l))?",
            "options": ["A) [1, 0, 2, ‘hello’, ”, []]", "B) Error", "C) [1, 2, ‘hello’]", "D) [1, 0, 2, 0, ‘hello’, ”, []]"],
            "answer": "C"
        },
         {
            "question 18": "Which of the following functions is a built-in function in python?",
            "options": ["A) factorial()", "B) print()", "C) seed()", "D) sqrt()"],
            "answer": "B"
        },
        {
            "question 19": "Which of the following is the use of id() function in python?",
            "options": ["A) Every object doesn’t have a unique id", "B) Id returns the identity of the object", "C) All of the mentioned", "D) None of the mentioned"],
            "answer": "B"
        },
        {
            "question 20": "The following python program can work with ____ parameters.?
             def f(x):
                def f1(*args, **kwargs):
                    print("Sanfoundry")
                    return x(*args, **kwargs)
                return f1",
            "options": ["A) any number of", "B) 0", "C) 1", "D) 2"],
            "answer": "A"
        },
        {
            "question 21": "What will be the output of the following Python function? 
            min(max(False,-3,-4), 2,7)",
            "options": ["A) -4", "B) -3", "C) 2", "D) False"],
            "answer": "D"
        },
        {
            "question 22": "Which of the following is not a core data type in Python programming?",
            "options": ["A) Tuples", "B) Lists", "C) Class", "D) Dictionary"],
            "answer": "C"
        },
        {
            "question 23": "What will be the output of the following Python expression if x=56.236? 
            print("%.2f"%x)",
            "options": ["A) 56.236", "B) 56.23", "C) 56.0000", "D) 56.24"],
            "answer": "B"
        },
        {
            "question 24": "Which of these is the definition for packages in Python?",
            "options": ["A) A set of main modules", "B) A folder of python modules", "C) A number of files containing Python definitions and statements", "D) A set of programs making use of Python modules"],
            "answer": "B"
        },
        {
            "question 25": "What will be the output of the following Python function? 
            len(["hello",2, 4, 6])",
            "options": ["A) Error", "B) 6", "C) 4", "D) 3"],
            "answer": "C"
        },
    ]
    return questions
