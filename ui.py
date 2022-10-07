from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score:',bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.current_question = self.canvas.create_text(
                    150, 
                    120, 
                    width=280,
                    text='jab jeb', 
                    font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, command=self.false_answer)
        self.false_button.grid(column=1, row=2)
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, command=self.true_answer)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.current_question, text=q_text)
        else:
            self.canvas.itemconfig(self.current_question, text="Out of questions")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)