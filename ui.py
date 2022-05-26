from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Hi",
                                                     font=FONT, width=270)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text=f"Score: {self.quiz_brain.score}")
        self.score.config(bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.yes_img = PhotoImage(file="images/true.png")
        self.no_img = PhotoImage(file="images/false.png")
        self.yes_button = Button(image=self.yes_img, highlightthickness=0,
                                 background=THEME_COLOR, command=self.yes)
        self.no_button = Button(image=self.no_img, highlightthickness=0,
                                background=THEME_COLOR, command=self.no)
        self.yes_button.grid(row=2, column=0)
        self.no_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def yes(self) -> str:
        if self.quiz_brain.check_answer("true"):
            self.correct_feedback()
            self.score.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.wrong_feedback()

        # else:
        #     new_message = messagebox.showinfo(title="Score")

    def no(self) -> str:
        if self.quiz_brain.check_answer("false"):
            self.correct_feedback()
            self.score.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.wrong_feedback()


    def original_canvas(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.get_next_question()
        else:
            message = f"You have reached the end of the quiz.\nYour score is " \
                      f"{self.quiz_brain.score}/{self.quiz_brain.question_number}"
            self.canvas.itemconfig(self.question_text, text=message)
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
    def correct_feedback(self):
        self.canvas.config(bg="green")
        self.window.after(1000, func=self.original_canvas)

    def wrong_feedback(self):
        self.canvas.config(bg="red")
        self.window.after(1000, func=self.original_canvas)
