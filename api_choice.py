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

        self.date_formatted = f"{self.date_today.month}/{self.date_today.day}/{self.date_today.year}"
        print(self.date_formatted)
        self.minsize(800, 800)
        self.key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
        self.api_list = StringVar()
        self.data_names = []
        self.food_var = StringVar()
        self.name_var = StringVar()
        self.protein_var = StringVar()
        self.calorie_var = StringVar()

        self.temp_dict = {
            self.date_formatted: {}
        }

        self.create_entry()
        self.custom_input()
        self.day_info()

    def create_entry(self):

        food_search = Entry(self, bd=10, textvariable=self.food_var, width=40)
        food_search.grid(row=0, column=0)

        food_submit = Button(self, bd=10, text='Search', command=lambda: self.api_search(self.food_var.get()))
        food_submit.grid(row=0, column=1)

        self.food_choices = Listbox(self, height=10, listvariable=self.api_list, width=40)
        self.food_choices.grid(row=1, column=0)


        food_choice_sub = Button(self, bd=10, text='Yum!!',
                                 command=lambda: self.nutrition_info(self.food_choices.get(ANCHOR)[1]))

        # The nutrition_info function needs work!
        food_choice_sub.grid(row=2, column=0)

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

    def custom_input(self):

        name_entry = Entry(self, bd=10, textvariable=self.name_var)
        name_entry.grid(row=4, column=0)

        protein_entry = Entry(self, bd=10, textvariable=self.protein_var)
        protein_entry.grid(row=4, column=1)

        calorie_entry = Entry(self, bd=10, textvariable=self.calorie_var)
        calorie_entry.grid(row=4, column=2)

        food_label = Label(self, text="Food")
        food_label.grid(row=3, column=0)

        protein_label = Label(self, text="Protein")
        protein_label.grid(row=3, column=1)

        calorie_label = Label(self, text="Calories")
        calorie_label.grid(row=3, column=2)

        save_button = Button(self, text="Save", command=lambda: self.tempsave())
        save_button.grid(row=4, column=3)

    def day_info(self):

        info_display = Canvas(self, bd=10, background='white')
        info_display.grid(row=5, column=0)

        text_format = self.temp_dict[self.date_formatted]

        for item in self.temp_dict[self.date_formatted]:
            text_format = item
        info_text = info_display.create_text()

    def tempsave(self):

        format_data = {
            self.name_var.get(): {"Protein": self.protein_var.get(), "Calories": self.calorie_var.get()}
        }

        self.temp_dict[self.date_formatted].update(format_data)


        # information = {
        #     '12/1/2021': {'Steak': {'Protein': 30, 'Calories': 500},
        #                   'Chicken': {'Protein': 30, 'Calories': 300}},
        # }










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

