from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="Question",
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(
            image=wrong_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.question_false
        )
        self.wrong_button.grid(row=2, column=0)
        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(
            image=correct_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.question_true
        )
        self.correct_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def question_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def question_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

