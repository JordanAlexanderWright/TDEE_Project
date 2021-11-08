from tkinter import *
from tkinter import ttk
import calendar
from datetime import date

class CalWindow(Tk):

    # I believe that when I am importing this it is still making another master frame. Need to work on that.

    def __init__(self, frame=NONE):
        super().__init__()

        # self.title("Calendar")
        # self.minsize(500, 400)
        # self.wm_iconbitmap("resources/atom.ico")
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

        self.create_calendar()



        self.style = ttk.Style(self)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)

    def create_calendar(self):

        try:
            self.store_selections()
        except:
            pass

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

        self.months = StringVar()
        self.month_box = ttk.Combobox(self.anchor_point, width=20, textvariable=self.months)
        self.month_box["values"] = list(self.month_dict.keys())

        # "values" here is not just creating a key : value pair. it's a keyword to set on combo_boxes.

        try:
            self.month_box.current(self.month_dict[self.month_selection] - 1)
        except AttributeError:
            self.month_box.current((self.today.month - 1))

        # This is a check to see if another month is selected, if not makes a default selection of current month
        # Wrapped in try block because month_selection doesn't exist on first pass

        self.month_box.grid(column=3, row=0, pady=(0, 40))

        self.year_entry = Entry(self.anchor_point, width=20)

        try:
            self.year_entry.insert(0, str(self.year_selection))
        except AttributeError:
            self.year_entry.insert(0, str(self.today.year))

        self.year_entry.grid(column=2, row=0, pady=(0,40))

        self.store_selections()

        # This code allows the user to input a year they want to see.
        # insert allows me to make a default input.

        self.date_submit = ttk.Button(self.anchor_point, text="Submit", command=lambda: self.create_calendar())
        self.date_submit.grid(column=4, row=0, pady=(0, 40))

        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        column_count = 0

        for day in days:
            label = Label(master=self.anchor_point, text=day)
            label.grid(column=column_count, row=1)
            column_count += 1

    def store_selections(self):

        self.month_selection = self.month_box.get()
        self.year_selection = self.year_entry.get()


        # This creates two variables that I use to figure out the selection of month and year. Default values will be
        # set at the current year and month.

    def date_buttons(self):

        month_var = self.month_dict[self.month_box.get()]
        year_var = int(self.year_entry.get())

        # This creates two variables that I use to figure out the selection of month and year. Default values will be
        # set at the current year and month.

        month_info = calendar.monthrange(year_var, month_var)
        num_days = month_info[1]

        if month_info[0] < 6:
            column_track = month_info[0] + 1
        if month_info[0] == 6:
            column_track = 0

        row_track = 2

        # This bit of code creates the starting place for the following code to start populating at. IE lets the
        # Calendar start at the right day of the week. Row track places it always beginning after the other info

        for day in range(1, num_days+1):
            date_as_str = str(day)
            btn = ttk.Button(master=self.anchor_point, text=date_as_str, style='Date.TButton', command=self.date_entry)
            btn.grid(column=column_track, row=row_track)
            column_track += 1

            if column_track == 7:
                column_track = 0
                row_track += 2

    def date_entry(self):

        self.temp_window = Toplevel(self.anchor_point)
        self.temp_window.minsize(500, 400)
        self.temp_window.title("Date Window")
        self.temp_window.name = StringVar()
        # self.text_entry()
        self.create_combo()
        self.create_label()
        self.create_button()

        # this is creating a new window in which a user can interact with. Just a placeholder for now.

    def create_combo(self):

        self.months = StringVar()
        self.temp_window.combo_box = ttk.Combobox(self.temp_window, width=20, textvariable=self.months)

        #"values" here is not just creating a key : value pair. it's a keyword to set on combo_boxes.
        #.current sets a default value for the box

        month_list = ("January", "February", "March", "April", "May", "June", "July", "August",
                  "September", "October", "November", "December")
        self.temp_window.combo_box["values"] = month_list
        self.temp_window.combo_box.current(0)
        self.temp_window.combo_box.grid(column=0, row=1, padx=0)

    def create_label(self):
        self.temp_window.label = Label(self.temp_window, text="What month do you want to see?")
        self.temp_window.label.grid(column=0, row=0)

        self.temp_window.label_answer = Label(self.temp_window, text="")
        self.temp_window.label_answer.grid(column=0, row=2)

    def create_button(self):
        self.temp_window.button = Button(self.temp_window, text="Submit response", command=self.click_button, padx=0)
        self.temp_window.button.grid(column=1, row=1)

    def click_button(self):
        answer = self.months.get()
        self.temp_window.button.config(text="Thanks!")
        self.temp_window.label_answer.config(text=f"I see that you picked {answer}")


if __name__ == '__main__':
    window = CalWindow()
    window.mainloop()