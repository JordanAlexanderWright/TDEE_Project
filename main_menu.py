from tkinter import *
from tkinter import ttk
import calendar_module

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("TDEE Main Menu")
        self.minsize(1920, 1080)
        self.wm_iconbitmap("resources/atom.ico")
        self.frame_var = Frame(self, background='grey')
        self.frame_var.pack(expand=True)
        self.menu_buttons(self.frame_var)
        self.create_menu()

        self.style = ttk.Style(self)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)
        self.style.configure('Date.TButton', foreground='green', padding=50)
        self.style.configure('Month.TLabel', foreground='orange', underline=True)
        self.style.configure('Menu.TButton',
                             background='grey',
                             foreground='black',
                             highlightthickness='30',
                             font=('Helvetica', 18, 'bold'))
        self.style.map('Menu.TButton',
                       foreground=[('disabled', '#B8B8B8'),
                                   ('pressed', 'black'),
                                   ('active', 'black')],
                       background=[('disabled', '#B8B8B8'),
                                   ('pressed', '!focus', '#C1C1C1'),
                                   ('active', 'white')],
                       highlightcolor=[('focus', '#A1A1A1'),
                                       ('!focus', 'white')],
                       relief=[('pressed', 'groove'),
                               ('!pressed', 'ridge')])

    # def frame_maker(self, frame_var="menu"):
    #
    #     self.frame_var = Frame(self, background='red')
    #     self.frame_var.pack()

    def menu_buttons(self, frame):
        self.current_week = ttk.Button(frame, text='Current Week', command=None, style='Menu.TButton')
        self.current_week.grid(column=1, row=1, padx=30, pady=30)

        self.current_month = ttk.Button(frame, text='Current Month', command=lambda: self.goto_calendar(frame), style='Menu.TButton')
        self.current_month.grid(column=1, row=2, padx=30, pady=30)

        self.log_lookup = ttk.Button(frame, text='Logging lookup', command=lambda: frame.destroy(), style='Menu.TButton')
        self.log_lookup.grid(column=1, row=3, padx=30, pady=30)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

    def goto_calendar(self, frame):
        frame.destroy()
        self.frame_var = Frame(self, background='grey')
        self.frame_var.pack(expand=True)
        stuff = calendar_module.CalWindow(self.frame_var)

    #     asdf = testing.CalendarGui(self.frame_var)
    #     asdf.do_stuff(self.frame_var)
    #     # NOW I NEED LOGIC TO OPEN THE CALENDAR MODULE STUFF


    def create_menu(self):

        self.menubar = Menu(self, tearoff=0)
        self.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.close_menu)
        self.file_menu.add_command(label="new", command=self.new_window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open")

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(labe="About")

    def close_menu(self):
        self.quit()
        self.destroy()

    def new_window(self):
        self.create_menu()

window = Window()
window.mainloop()
