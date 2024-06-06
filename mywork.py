   
import random
import tkinter as tk
from tkinter import ttk, messagebox

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
    {
        "question": "How many days are there in a year?",
        "options": ["100", "200", "365", "366"],
        "answer": "365"
    },
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
        "options": ["Python", "JavaScript", "HTML", "MySQL"],
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
        "type": "trueFalse",
        "question": "The Earth is flat.",
        "options": ["True", "False"],
        "answer": "False"
    }
]

class QuizApp:
   def __init__(self, root):
    self.root = root
    self.root.title("Quiz Application")
    
    # Set the total time in minutes
    self.total_time_minutes = 5  # Example: 5 minutes
    self.total_time_seconds = self.total_time_minutes * 60
    
    self.time_remaining = self.total_time_seconds
    self.score = 0
    self.current_question_index = 0

    self.timer_label = tk.Label(root, text=f"Time Remaining: {self.time_remaining} seconds")
    self.timer_label.pack()

    self.question_label = tk.Label(root, text="", wraplength=400)
    self.question_label.pack()

    self.option_vars = []
    self.option_buttons = []

    for _ in range(4):
        var = tk.StringVar()
        button = tk.Radiobutton(root, variable=var, value="", text="", command=self.check_answer)
        button.pack(anchor=tk.W)
        self.option_vars.append(var)
        self.option_buttons.append(button)

    self.result_label = tk.Label(root, text="")
    self.result_label.pack()

    self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
    self.start_button.pack()

    self.progress_var = tk.DoubleVar()
    self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
    self.progress_bar.pack(fill=tk.X, expand=1)

    def start_quiz(self):
        self.start_button.pack_forget()
        self.show_question()
        self.start_timer()
        self.start_progress_bar()

    def show_question(self):
        question = questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        
        for var, button, option in zip(self.option_vars, self.option_buttons, question["options"]):
            var.set(option)
            button.config(text=option, value=option, state=tk.NORMAL)

        self.result_label.config(text="")

    def start_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time Remaining: {self.time_remaining} seconds")
            self.root.after(1000, self.start_timer)
        else:
            self.end_quiz()

    def start_progress_bar(self):
        progress_increment = 100 / self.total_time_seconds
        current_progress = self.progress_var.get()
        if current_progress < 100:
            self.progress_var.set(current_progress + progress_increment)
            self.root.after(1000, self.start_progress_bar)
        else:
            self.end_quiz()

def check_answer(self):
    question = questions[self.current_question_index]
    selected_option = next((var.get() for var in self.option_vars if var.get()), None)
    
    if selected_option:
        if selected_option == question["answer"]:
            self.score += 1
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Incorrect. The correct answer is {question['answer']}")
    else:
        self.result_label.config(text="You did not select an answer.")
    
    self.disable_buttons()
    self.current_question_index += 1
    
    if self.current_question_index < len(questions):
        self.root.after(2000, self.show_question)
    else:
        self.root.after(2000, self.end_quiz)

    def disable_buttons(self):
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

    def end_quiz(self):
        self.disable_buttons()
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score} out of {len(questions)}.")
        self.result_label.config(text=f"Your final score is {self.score} out of {len(questions)}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
