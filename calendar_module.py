from tkinter import *
from tkinter import ttk
from calendar import monthrange
from datetime import date
import api_choice


class CalWindow(Toplevel):

    # I need to  use Toplevel for any new windows. Can only have one Tk window.

    def __init__(self, frame=NONE):
        super().__init__()

        # setting a few default variables

        self.anchor_point = frame
        self.month_dict = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        self.today = date.today()
        self.months = StringVar()

        # Creating a style object to apply to the calendar

        self.style = ttk.Style(self)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)

        self.create_calendar()

    def create_calendar(self):

        try:
            self.store_selections()
        except:
            print("Hello, some kind of error happened")

        if self.anchor_point == NONE:
            self.anchor_point = Frame(self, background='grey')
            self.anchor_point.pack(expand=True)
        else:
            self.anchor_point.destroy()
            self.anchor_point = Frame(self, background='grey')
            self.anchor_point.pack(expand=True)

        self.date_labels()
        self.date_buttons()

    def date_labels(self):

        # "values" here is not just creating a key : value pair. it's a keyword to set on combo_boxes.

        self.month_box = ttk.Combobox(self.anchor_point, width=20, textvariable=self.months)
        self.month_box["values"] = list(self.month_dict.keys())

        # This is a check to see if another month is selected, if not makes a default selection of current month
        # Looking for AttributeError in try block because month_selection doesn't exist on first pass

        try:
            self.month_box.current(self.month_dict[self.month_selection] - 1)
        except AttributeError:
            self.month_box.current((self.today.month - 1))

        self.year_entry = Entry(self.anchor_point, width=20)

        # insert allows me to make a default input.

        self.year_entry = Entry(self.anchor_point, width=20)

        try:
            self.year_entry.insert(0, str(self.year_selection))
        except AttributeError:
            self.year_entry.insert(0, str(self.today.year))

        self.month_box.grid(column=3, row=0, pady=(0, 40))
        self.year_entry.grid(column=2, row=0, pady=(0, 40))

        self.store_selections()

        # This code allows the user to input a year they want to see.

        self.date_submit = ttk.Button(self.anchor_point, text="Submit", command=lambda: self.create_calendar())
        self.date_submit.grid(column=4, row=0, pady=(0, 40))

        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        column_count = 0

        for day in days:
            label = Label(master=self.anchor_point, text=day)
            label.grid(column=column_count, row=1)
            column_count += 1

    def store_selections(self):

        # This creates two variables that I use to figure out the selection of month and year. Default values will be
        # set at the current year and month.

        self.month_selection = self.month_box.get()
        self.year_selection = self.year_entry.get()
        self.day_selection = StringVar

    def date_buttons(self):

        # This creates two variables that I use to figure out the selection of month and year. Default values will be
        # set at the current year and month.

        month_select = self.month_dict[self.month_box.get()]
        year_select = int(self.year_entry.get())

        # Using the Calendar module this gives me the weekday of the first day of the month and number of days
        # in the selected month / year

        month_info = monthrange(year_select, month_select)
        num_days = month_info[1]

        # This bit of code creates the starting place for the following code to start populating at. IE lets the
        # Calendar start at the right day of the week. Row track places it always beginning after the other info

        if month_info[0] < 6:
            column_track = month_info[0] + 1
        if month_info[0] == 6:
            column_track = 0

        row_track = 2

        for day in range(1, num_days+1):
            date_as_str = str(day)

            btn = ttk.Button(master=self.anchor_point, text=date_as_str, style='Date.TButton',
                             command=lambda day=day, month=self.month_selection, year=self.year_selection:
                             api_choice.FoodSearch(day, month, year))

            btn.grid(column=column_track, row=row_track)
            column_track += 1

            if column_track == 7:
                column_track = 0
                row_track += 2

        # The lambda function is black freaking magic.
        # Reference: https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments


if __name__ == '__main__':
    window = CalWindow()
    window.mainloop()
