from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.q_text = None
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)

        self.label = Label(text=f"score: 0", font=("Helvetica", 15), fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 130, width=280, text="Quizzler", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(self.window, image=self.true_image, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(self.window, image=self.false_image, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=self.q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(background="green")
            self.score += 1
            self.label.config(self.label, text=f"score: {self.score}")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
