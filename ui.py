from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.quiz_end = False
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_txt = self.canvas.create_text(150,
                                                    125,
                                                    width=280,
                                                    fill=THEME_COLOR,
                                                    text="some text",
                                                    font=("Arial", 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.check_img,
                                   highlightthickness=0,
                                   command=self.true_button,
                                   pady=20,
                                   padx=20)
        self.check_button.grid(row=2, column=0)

        self.cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_img,
                                   highlightthickness=0,
                                   command=self.false_button,
                                   pady=20,
                                   padx=20)
        self.cross_button.grid(row=2, column=1)

        self.score_txt = Label(text=f"Score: {self.score}",
                               font=("Times New Roman", 14, "bold"),
                               bg=THEME_COLOR,
                               fg="white")
        self.score_txt.grid(column=1, row=0)
        self.set_question()
        self.window.mainloop()

    def give_feedback(self, gain):
        if gain == 1:
            self.canvas.config(bg="green")
            self.window.after(300, self.set_question)
        elif gain == 0:
            self.canvas.config(bg="red")
            self.window.after(300, self.set_question)

    def true_button(self):
        if not self.quiz_end:
            answer = "True"
        else:
            return
        gain = self.quiz.check_answer(answer)
        self.score += gain
        self.score_txt.config(text=f"Score: {self.score} / {self.quiz.question_number}")
        self.give_feedback(gain)

    def false_button(self):
        if not self.quiz_end:
            answer = "False"
        else:
            return
        gain = self.quiz.check_answer(answer)
        self.score += gain
        self.score_txt.config(text=f"Score: {self.score} / {self.quiz.question_number}")
        self.give_feedback(gain)

    def set_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = f"True / False:\n\n{self.quiz.next_question()}"
            self.canvas.itemconfig(self.question_txt, text=question)
        else:
            self.canvas.itemconfig(self.question_txt, text="Quiz Completed")
            self.quiz_end = True
