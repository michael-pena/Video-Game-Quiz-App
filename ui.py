import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score
        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.question_canvas = tkinter.Canvas(bg="White", height=250, width=300)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.question_canvas.create_text(150, 125, text="Some text",
                                                              fill=THEME_COLOR, font=("Arial", 20),
                                                              width=280)

        # Correct Button
        self.correct_image = tkinter.PhotoImage(file="images/true.png")
        self.correct_button = tkinter.Button(image=self.correct_image, command=self.submit_true)
        self.correct_button.grid(row=2, column=0)

        # Incorrect Button
        self.incorrect_image = tkinter.PhotoImage(file="images/false.png")
        self.incorrect_button = tkinter.Button(image=self.incorrect_image, command=self.submit_false)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"score: {self.quiz.score}")
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz! "
                                                                     f"You scored: {self.quiz.score} / {len(self.quiz.question_list)}")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def submit_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def submit_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        self.window.after("1000", self.get_next_question)



