from tkinter import *
from tkinter import ttk
import calendar
from datetime import date

class CalWindow(Tk):

    def __init__(self, frame=NONE):
        super().__init__()

        # self.title("Calendar")
        # self.minsize(500, 400)
        # self.wm_iconbitmap("resources/atom.ico")
        if frame == NONE:
            self.anchor_point = self
        else:
            self.anchor_point = frame

        self.today = date.today()
        self.date_labels()
        self.date_buttons()
        self.style = ttk.Style(self)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)

    def date_labels(self):


        month_dict = {
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


        self.months = StringVar()
        self.month_box = ttk.Combobox(self.anchor_point, width=20, textvariable=self.months)
        self.month_box["values"] = list(month_dict.keys())
        # self.month_box.current = (list(month_dict)[(self.today.month - 1)])
        self.month_box.current((self.today.month - 1))
        self.month_box.grid(column=3, row=0, pady=(0, 40))

        self.year_entry = Entry(self.anchor_point, width=20)
        self.year_entry.insert(0, "2021")
        self.year_entry.grid(column=2, row=0, pady=(0,40))

        self.date_submit = ttk.Button(self.anchor_point, command=self.date_buttons())

        #"values" here is not just creating a key : value pair. it's a keyword to set on combo_boxes.
        #.current sets a default value for the box

        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        column_count = 0

        for day in days:
            label = Label(master=self.anchor_point, text=day)
            label.grid(column=column_count, row=1)
            column_count += 1

    def date_buttons(self):

        month_dict = {
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


        month_selection = month_dict[self.months.get()]
        year_selection = int(self.year_entry.get())

        month_info = calendar.monthrange(year_selection, month_selection)
        num_days = month_info[1]
        if month_info[0] < 6:
            column_track = month_info[0] + 1
        if month_info[0] == 6:
            column_track = 0
        row_track = 2

        for day in range(1, num_days+1):
            date_as_str = str(day)
            btn = ttk.Button(master=self.anchor_point, text=date_as_str, style='Date.TButton', command=self.date_entry)
            btn.grid(column=column_track, row=row_track)
            column_track += 1

            if column_track == 7:
                column_track = 0
                row_track += 2

    def date_info(self):
        month_selection = self.month_box.get()
        month_info = calendar.monthrange(self.today.year, self.today.month-1)


    def date_entry(self):

        self.temp_window = Toplevel(self.anchor_point)
        self.temp_window.minsize(500, 400)
        self.temp_window.title("Date Window")
        self.temp_window.name = StringVar()
        # self.text_entry()
        self.create_combo()
        self.create_label()
        self.create_button()

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