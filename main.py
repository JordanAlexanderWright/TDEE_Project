from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("TDEE Calculator")
        self.minsize(500, 400)
        self.wm_iconbitmap("resources/atom.ico")
        self.create_calendar_choice()
        self.create_options()

    def create_options(self):
        self.option1 = ttk.Button(self, text="Input Food")
        self.option2 = ttk.Button(self, text="See Calendar")
        self.option3 = ttk.Button(self, text="Today's Stats")

        option_list = [self.option1, self.option2, self.option3]

        for iter, option in enumerate(option_list):
            option.grid(column=0, row=(iter + 1))

    def create_calendar_choice(self):
        self.btn1 = ttk.Button(self, text="Open Choice Box", command=self.choice_box)
        self.btn1.grid(column=0, row=0)

    def choice_box(self):
        answer = msgbox.askyesnocancel(title="MultipleChoiceBox", message="Do you want to quit?")

        if answer == True:
            self.quit()

window = Window()
window.mainloop()