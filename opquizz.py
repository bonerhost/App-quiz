import random
questions = [
   {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Performance Unit", "Central Program Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["Random Access Memory", "Read Access Memory", "Ready Access Memory", "Randomized Access Memory"],
        "answer": "Random Access Memory"
    },
    {
        "question": "What is the main function of an operating system?",
        "options": ["To manage hardware and software resources", "To create documents", "To browse the internet", "To perform calculations"],
        "answer": "To manage hardware and software resources"
    },
    {
        "question": "What is the name of the first computer virus?",
        "options": ["Creeper", "ILOVEYOU", "Mydoom", "Melissa"],
        "answer": "Creeper"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["Hypertext Transfer Protocol", "Hyperlink Transfer Protocol", "Hypertext Transmission Protocol", "Hyperlink Transmission Protocol"],
        "answer": "Hypertext Transfer Protocol"
    },
    {
        "question": "Which of these is not a programming language?",
        "options": ["Python", "Java", "HTML", "MySQL"],
        "answer": "MySQL"
    },
    {
        "question": "What does DNS stand for?",
        "options": ["Domain Name System", "Digital Network System", "Domain Network Service", "Digital Name Service"],
        "answer": "Domain Name System"
    },
    {
        "question": "What is the purpose of a firewall in computer networks?",
        "options": ["To block unauthorized access", "To accelerate network speed", "To store data", "To compress files"],
        "answer": "To block unauthorized access"
    },
    {
        "question": "What is the main use of SQL?",
        "options": ["Web development", "Database management", "Operating system development", "Graphics design"],
        "answer": "Database management"
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["Apple", "IBM", "Microsoft", "Google"],
        "answer": "Microsoft"
    },
    {
        "question": "What does IP stand for in networking?",
        "options": ["Internet Protocol", "Internet Provider", "Internal Protocol", "Internal Provider"],
        "answer": "Internet Protocol"
    },
    {
        "question": "What is the primary function of a router?",
        "options": ["To store data", "To manage power supply", "To connect multiple networks", "To display graphics"],
        "answer": "To connect multiple networks"
    },
    {
        "question": "Which programming language is known for its use in artificial intelligence and machine learning?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "What does URL stand for?",
        "options": ["Uniform Resource Locator", "Uniform Resource Link", "Universal Resource Locator", "Universal Resource Link"],
        "answer": "Uniform Resource Locator"
    },
    {
        "question": "What is the main purpose of an IDE in programming?",
        "options": ["To compile code", "To debug code", "To provide a development environment", "To manage databases"],
        "answer": "To provide a development environment"
    },
    {
        "question": "Which company is known for the Android operating system?",
        "options": ["Apple", "Microsoft", "Google", "IBM"],
        "answer": "Google"
    },
    {
        "question": "What does SSD stand for in computer storage?",
        "options": ["Solid State Drive", "Super Speed Drive", "Small Storage Device", "Solid Storage Disk"],
        "answer": "Solid State Drive"
    },
    {
        "question": "Which of these is a NoSQL database?",
        "options": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"],
        "answer": "MongoDB"
    },
    {
        "question": "What is the main use of CSS in web development?",
        "options": ["To structure content", "To style web pages", "To create dynamic content", "To manage databases"],
        "answer": "To style web pages"
    },
    {
        "question": "What does GUI stand for?",
        "options": ["Graphical User Interface", "General User Interface", "Graphical Universal Interface", "General Universal Interface"],
        "answer": "Graphical User Interface"
    },
    {
        "question": "What is the main purpose of an API?",
        "options": ["To create graphical content", "To manage operating systems", "To enable communication between software components", "To provide database storage"],
        "answer": "To enable communication between software components"
    },
    {
        "question": "Which technology is used for creating virtual machines?",
        "options": ["Docker", "Kubernetes", "Hypervisor", "Ansible"],
        "answer": "Hypervisor"
    },
    {
        "question": "What does VPN stand for?",
        "options": ["Virtual Private Network", "Virtual Public Network", "Virtual Protected Network", "Virtual Personal Network"],
        "answer": "Virtual Private Network"
    },
    {
        "question": "Which language is primarily used for data analysis and statistical computing?",
        "options": ["Python", "R", "Java", "C#"],
        "answer": "R"
    },
    {
        "question": "What is the purpose of version control systems like Git?",
        "options": ["To manage network security", "To manage software versions and collaboration", "To manage hardware resources", "To manage web hosting"],
        "answer": "To manage software versions and collaboration"
    },
    {
        "question": "Which of these is a popular JavaScript framework for building web applications?",
        "options": ["Django", "Flask", "Angular", "Spring"],
        "answer": "Angular"
    },
    {
        "question": "What does IoT stand for?",
        "options": ["Internet of Things", "Internet of Technology", "Integration of Technology", "Internet of Telecommunications"],
        "answer": "Internet of Things"
    },
    {
        "question": "Which protocol is commonly used to secure web transactions?",
        "options": ["FTP", "HTTP", "HTTPS", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "What does AI stand for?",
        "options": ["Artificial Interface", "Automatic Intelligence", "Artificial Intelligence", "Automated Interface"],
       "answer": "Artificial Intelligence"
    },
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
    {
        "type": "trueFalse",
        "question": "The Earth is flat.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "type": "shortAnswer",
        "question": "What is the chemical symbol for water?",
        "answer": "H2O"
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