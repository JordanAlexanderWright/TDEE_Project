from tkinter import *
from tkinter import ttk
import calendar


class Window(Tk):

    def __init__(self):
        super().__init__()

        self.title("Calendar")
        self.minsize(500, 400)
        self.wm_iconbitmap("resources/atom.ico")
        self.date_buttons()
        self.date_labels()
        self.style = ttk.Style(self)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)

    def date_labels(self):

        month = "October"
        month_label = ttk.Label(master=self, text=month, style='Month.TLabel')
        month_label.grid(column=3, row=0, pady=(0,40))

        october = calendar.monthrange(2021, 10)

        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        column_count = 0

        for day in days:
            label = Label(master=self, text=day)
            label.grid(column=column_count, row=1)
            column_count += 1

    def date_buttons(self):

        october = calendar.monthrange(2021, 10)
        num_days = october[1]
        column_track = october[0]
        row_track = 2

        for day in range(1, num_days+1):
            date_as_str = str(day)
            btn = ttk.Button(master=self, text=date_as_str, style='Date.TButton', command=self.date_entry)
            btn.grid(column=column_track, row=row_track)
            column_track += 1

            if column_track == 7:
                column_track = 0
                row_track += 2

    def date_entry(self):

        self.temp_window = Toplevel(self)
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

    def create_button(self, ):
        self.temp_window.button = Button(self.temp_window, text="Submit response", command=self.click_button, padx=0)
        self.temp_window.button.grid(column=1, row=1)

    def click_button(self):
        answer = self.months.get()
        self.temp_window.button.config(text="Thanks!")
        self.temp_window.label_answer.config(text=f"I see that you picked {answer}")


if __name__ == '__main__':
    window = Window()
    window.mainloop()