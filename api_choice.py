import requests
from tkinter import *
from tkinter import ttk

class Window(Tk):

    def __init__(self):
        super().__init__()

        self.title('Food Selection')
        self.minsize(800, 800)
        self.create_entry()

    def create_entry(self):
        food_var = StringVar()
        food_search = Entry(self, bd=10, textvariable=food_var, width=40)
        food_search.pack()

        food_submit = Button(self, bd=10, text='Search', command=lambda: print("I was clicked"))
        food_submit.pack()

        api_list = StringVar()
        api_list.set('Strawberry1 Strawberry2 Strawberry3')
        food_choices = Listbox(self, height=10, listvariable=api_list)
        food_choices.pack()

        print(type(api_list.get()))
        food_choice_sub = Button(self, bd=10, text='Yum!!', command=lambda: print(food_choices.get(ANCHOR)))
        food_choice_sub.pack()
#
# print("Please Input a food you'd like to lookup")
# food = input()
# my_key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
# query_type = 'list'
# payload = {'api_key': my_key, 'query': food}
# response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list", params=payload)
#
# print(response.status_code)
#
# information = response.json()

# response.json() here creates a list of dictionaries.
#
# keys = ['fdcId', 'description', 'dataType', 'brandOwner']
# for item in information:
#     for key in keys:
#         try:
#             print(item[key])
#         except KeyError:
#             print(f"There may be an error with this key:{key}")
#
#
#

window = Window()

window.mainloop()
# fdcId
# description
# dataType
# food_id = 2165595