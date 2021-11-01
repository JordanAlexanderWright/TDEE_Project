import datetime
import calendar
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import ttk

# I need to create a function that allows a user to select the month and year they want to view

# I then need to be able to turn that into usable date for the program
# Next, populate the calendar with the appropriate number of days, month name, whatever.


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("TDEE Calculator")
        self.minsize(500, 400)
        self.wm_iconbitmap("resources/atom.ico")
        self.text_entry()

    def text_entry(self):

        self.month = StringVar()
        self.year = StringVar()
        # This is creating a stringvariable object that allows you to manipulate information from a textbox

        self.month_label = ttk.Label(self, text="Enter The Desired Month")
        self.month_label.grid(column=1, row=1, sticky="n")

        self.monthbox = ttk.Entry(self, width=20, textvariable=self.month)
        # This will set the cursor already set on the textbox when the application is run
        self.monthbox.focus()
        self.monthbox.grid(column=1, row=2, sticky="n")

        self.month_button = ttk.Button(self, text="Submit", command=self.month_click)
        self.month_button.grid(column=1, row=3, sticky="n", pady=(0, 30))

        self.year_label = ttk.Label(self, text="Enter The Desired Year")
        self.year_label.grid(column=1, row=4, sticky="n")

        self.yearbox = ttk.Entry(self, width=20, textvariable=self.year)
        self.yearbox.grid(column=1, row=5, sticky="n")

        self.year_button = ttk.Button(self, text="Submit", command=self.year_click)
        self.year_button.grid(column=1, row=6, sticky="n")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(7, weight=1)

        # This shit is fucky -- have to mess with it. I set weight to the invisible rows/colums to take up extra space.

    def month_click(self):
        month = self.month.get()
        month_list = ("January", "February", "March", "April", "May", "June", "July", "August",
                  "September", "October", "November", "December")
        if month.title() not in month_list:
            self.month_label.config(text="Please submit a valid month")
        elif month.title() in month_list:
            self.month_label.config(text=f"You chose {month.title()}")

    def year_click(self):
        year = self.year.get()
        if year != int:
            self.year_label.config(text=f"Please Input an Integer")
        if len(str(year)) == 4:
            self.year_label.config(text=f"You chose {self.year.get()}")
        else:
            self.year_label.config(text="I don't know how, but you broke it, loser")
        # this sets up the code for the text boxes and layout


if __name__ == '__main__':
    window = Window()
    window.mainloop()