from tkinter import *
from tkinter import ttk
import calendar_module
import api_choice

class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("TDEE Main Menu")
        self.wm_iconbitmap("resources/atom.ico")

        # This sets the title of the windows, and maps the icon used in the top left of the app

        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()

        # This check the actual height and width of the display i'm using, although I end up letting the frames
        # Automatically size themselves for simplicity.

        # self.minsize(int(screen_width*(3/4)), int(screen_height*(3/4)))
        # self.maxsize(screen_width, screen_height)

        self.frame_var = Frame(self, background='grey')
        self.frame_var.pack(expand=True)

        # This is setting a frame for everything to be anchored to. Did this instead of the master frame
        # So that I can destroy the frame and refresh with new widgets / options rather than closing the app.

        self.menu_buttons(self.frame_var)
        self.create_menu()

        # This calls the function I made in the class. Makes the menu, passing the anchor frame.

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

        # Needs to be worked on, but I created a style object that allows me to make style templates for whatever
        # Object I need. the style.map is basically a more complicated version that allows me to work with TTK widgets.

    # def frame_maker(self, frame_var="menu"):
    #
    #     self.frame_var = Frame(self, background='red')
    #     self.frame_var.pack()

    def menu_buttons(self, frame):

        self.current_week = ttk.Button(frame, text='Current Week', command=lambda: self.goto_fill(frame), style='Menu.TButton')
        self.current_week.grid(column=1, row=1, padx=30, pady=30)

        self.current_month = ttk.Button(frame, text='Current Month', command=lambda: self.goto_calendar(frame),
                                        style='Menu.TButton')
        self.current_month.grid(column=1, row=2, padx=30, pady=30)

        self.log_lookup = ttk.Button(frame, text='Logging lookup', command=lambda: frame.destroy(),
                                     style='Menu.TButton')
        self.log_lookup.grid(column=1, row=3, padx=30, pady=30)

        # These lines create a set of menu options, need to be expanded on. Log lookup is a placeholder.

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        # I set the weight here because it will allow my widgets to fill the space. Also, this will cause all widgets
        # to be centered in the event the application is resized.

    def goto_fill(self, frame):
        frame.destroy()
        self.frame_var = Frame(self,background='grey')
        self.frame_var.pack(expand=True)
        trying = api_choice.FoodSearch(self.frame_var)

    def goto_calendar(self, frame):
        frame.destroy()
        self.frame_var = Frame(self, background='grey')
        self.frame_var.pack(expand=True)
        stuff = calendar_module.CalWindow(self.frame_var)

        # This will destroy the frame that whatever widgets i'm moving away from are anchored to.
        # this is importing from the calendar gui file, which handles all of the calendar interface.

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

        # All of this code creates a very basic menu (top left of the application)
        # This menu has little to no functionality, but needs to be expanded up.

    def close_menu(self):
        self.quit()
        self.destroy()

    def new_window(self):
        self.create_menu()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
