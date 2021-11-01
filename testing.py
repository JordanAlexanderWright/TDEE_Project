from tkinter import *
from tkinter import ttk

class CalendarGui():

    def __init__(self, frame):
        self.do_stuff(frame)

    def do_stuff(self, frame):

        self.current_week = ttk.Button(frame, text='Current Week', command=None, style='Menu.TButton')
        self.current_week.grid(column=1, row=1, padx=30, pady=30)

        self.current_month = ttk.Button(frame, text='Current Month', command=lambda: self.goto_calendar(frame),
                                        style='Menu.TButton')
        self.current_month.grid(column=1, row=2, padx=30, pady=30)

        self.log_lookup = ttk.Button(frame, text='Logging lookup', command=lambda: frame.destroy(),
                                     style='Menu.TButton')
        self.log_lookup.grid(column=1, row=3, padx=30, pady=30)

        print("I'm Working! I think")

if __name__ == '__main__':
    CalendarGui()