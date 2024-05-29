import random
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    # Add more questions here
]

# Function to start the quiz
def start_quiz():
    score = 0
    print("Welcome to the Interactive Quiz!")
    print("===============WELCOME=================")

    # Shuffle the questions randomly
    random.shuffle(questions)

    # Loop through each question
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            user_answer = question["options"][int(user_answer) - 1]
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}")
        else:
            print("Invalid input. Please try again.")

        print()  # Add a blank line for better readability

    print(f"Your final score is {score} out of {len(questions)}.")

# Run the quiz
start_quiz()

