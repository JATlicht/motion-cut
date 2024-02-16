import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jathin's Quiz")
        self.root.geometry("400x300")
        self.root.config(bg="black")

        self.questions = [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "NaCl", "CH4"],
                "answer": "H2O"
            },
            {
                "question": "What is the closest planet to the Sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": "Mercury"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic reticulum"],
                "answer": "Mitochondria"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer":"Au"
            },
            {
                "question":"What is the largest planet in our solar system?",
                "options":["Jupiter", "Saturn", "Earth", "Neptune"],
                "answer":"Jupiter"
            },
            {
                "question":"What is the boiling point of water in Celsius?",
                "options":["0", "100", "-100", "50"],
                "answer":"100"
            },
            {
                "question":"What is the speed of light in a vacuum? (in m/s)",
                "options":["299792458", "300000000", "200000000", "250000000"],
                "answer":"299792458"
            },
            {
                "question":"What is the chemical symbol for iron?",
                "options":["Fe", "Ir", "In", "Au"],
                "answer":"Fe"
            },
            {
                "question":"What is the atomic number of oxygen?",
                "options":["7", "8", "9", "6"],
                "answer":"8"
            },
            {
                "question":"What is the largest mammal in the world?",
                "options":["Blue whale", "African elephant", "Giraffe", "Hippopotamus"],
                "answer":"Blue whale"
            }

        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", bg="black", fg="white")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx), bg="black", fg="white")
            button.pack(fill=tk.BOTH, padx=10, pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0", bg="black", fg="white")
        self.score_label.pack()

        self.result_label = tk.Label(self.root, text="", bg="black", fg="white")
        self.result_label.pack()

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])

            for i in range(4):
                self.option_buttons[i].config(text=question["options"][i])

        else:
            if self.score == len(self.questions):
                messagebox.showinfo("Quiz Finished", f"Congratulations, you are a genius!\nYour final score: {self.score}/{len(self.questions)}")
            else:
                messagebox.showinfo("Quiz Finished", f"Your final score: {self.score}/{len(self.questions)}")
            self.root.destroy()

    def check_answer(self, selected_index):
        question = self.questions[self.current_question]
        if question["options"][selected_index] == question["answer"]:
            self.option_buttons[selected_index].config(bg="green")
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.option_buttons[selected_index].config(bg="red")
            self.result_label.config(text="Incorrect", fg="red")

        self.current_question += 1
        self.update_score_label()
        self.root.after(1000, self.reset_button_colors)  # Reset button colors after 1 second
        self.root.after(1000, self.update_question)    # Move to the next question after 1 second

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}")

    def reset_button_colors(self):
        for button in self.option_buttons:
            button.config(bg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
