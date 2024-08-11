REPOSITORY DESCRIPTION:
Repository Name: CLI-Quiz-Application

This repository contains a Python-based Command Line Interface (CLI) quiz application. 
The quiz allows users to answer a series of multiple-choice questions, randomly selected
from a predefined set. The application tracks the user's score and provides a success or
fail result based on a pass mark. The project is modular, with code divided into different
Python modules to handle various functionalities like question management, quiz logic, and
result computation. The project is also collaboratively developed with multiple contributors.

README.md:

# CLI-Quiz-Application

## DESCRIPTION
The CLI-Quiz-Application is a Python-based command line tool that presents users with a
multiple-choice quiz. The quiz pulls questions randomly from a predefined set, tracks 
the user's answers, and calculates the final score. The application is modular and easy
to extend, with separate modules for handling questions, quiz logic, and scoring. 
The user is evaluated based on a pass mark, and the results are displayed at the end 
of the quiz.

## FEATURES
- Random selection of questions using Python's `random` module.
- Modular code structure for easy maintenance and extension.
- Tracks and displays the user's score.
- Pass/fail evaluation based on a set pass mark.

## How to Start
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/CLI-Quiz-Application.git
   cd CLI-Quiz-Application
Install Required Dependencies
The application requires Python 3.x. Install any necessary dependencies using
pip (if applicable).

Run the Quiz
Execute the main Python script to start the quiz:

python main.py
How to Use
Once the quiz starts, you will be presented with multiple-choice questions.
Type the letter corresponding to your chosen answer and press Enter.
The quiz continues until all questions have been answered.
At the end of the quiz, your score is displayed, along with a success or fail 
message based on a pass mark of 15 out of 25.
Example

Question 1:Which type of Programming does Python support?

a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned
Answer: d

Your answer: c
Correct!

...

You scored 18 out of 25.
Congratulations, you passed!

MODULES
main.py: The entry point of the application. It handles the flow of the quiz.
questions.py: Contains the list of questions and correct answers.
quiz.py: Manages the quiz logic, including random question selection and score tracking.
results.py: Handles the final scoring and result presentation.
utils.py: Utility functions for validation and input handling.
Contributing
We welcome contributions from the community. Please fork the repository and create a
pull request for any features, enhancements, or bug fixes. Ensure that your code 
follows the project's style guide and is thoroughly tested.

AUTHORS
Kwagfan Aondover Amos - Initial work - User ID-24834
Contributor Name - Additional features - contributor-username

This README provides an overview of the repository, instructions on how to set up and
run the quiz, and details about the modules and contributors. It serves as a 
comprehensive guide for users and contributors to the project.
