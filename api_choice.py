import requests
from tkinter import *
from tkinter import ttk
from datetime import date


class FoodSearch(Toplevel):

    def __init__(self, day=None, month=None, year=None, frame=None,):
        super().__init__()

        print(day, month, year)
        self.date_today = date.today()

        self.month_list = ("January", "February", "March", "April", "May", "June", "July", "August",
                      "September", "October", "November", "December")

        if day and month and year == True:
            self.title(f"{month}-{day}, {year}")
        else:
            self.title(f"{self.month_list[self.date_today.month-1]} {self.date_today.day}, {self.date_today.year}")

        self.minsize(800, 800)
        self.key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
        self.api_list = StringVar()
        self.data_names = []
        self.food_var = StringVar()

        self.create_entry()

    def create_entry(self):

        food_search = Entry(self, bd=10, textvariable=self.food_var, width=40)
        food_search.pack()

        food_submit = Button(self, bd=10, text='Search', command=lambda: self.api_search(self.food_var.get()))
        food_submit.pack()

        self.food_choices = Listbox(self, height=10, listvariable=self.api_list)
        self.food_choices.pack()


        food_choice_sub = Button(self, bd=10, text='Yum!!',
                                 command=lambda: self.nutrition_info(self.food_choices.get(ANCHOR)[1]))

        # The nutrition_info function needs work!
        food_choice_sub.pack()

    def api_search(self, search_param):

        print(search_param)
        payload = {'api_key': self.key, 'query': search_param, 'requireAllWords': True, 'pageSize': 5,
                   'dataType': ['Branded']}
        response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=payload)
        data = response.json()

        for food in data['foods']:
            print(food)
            print(food['lowercaseDescription'])
            self.data_names.append(f"{food['lowercaseDescription'].title()}: {food['brandOwner']}")

        self.api_list.set(self.data_names)
        for item in self.data_names:
            print(item)
        print("Hello")

    def nutrition_info(self, fcdid):

        payload = {'api_key': self.key}
        response = requests.get(f"https://api.nal.usda.gov/fdc/v1/food/{fcdid}", params=payload)
        data = response.json()

        # This Function needs work, the payload params probably don't apply here

        for item in data:
            print(item)

        try:
            print(data['servingSize'])
        except:
            pass
        try:
            print(data['labelNutrients'])
        except:
            pass












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


if __name__ == "__main__":
    window = FoodSearch()
    window.mainloop()

