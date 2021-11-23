import requests
from tkinter import *
from tkinter import ttk


class Window(Tk):

    def __init__(self):
        super().__init__()

        self.title('Food Selection')
        self.minsize(800, 800)
        self.key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
        self.api_list = StringVar()
        self.data_names = []

        self.create_entry()

    def create_entry(self):
        food_var = StringVar()
        food_search = Entry(self, bd=10, textvariable=food_var, width=40)
        food_search.pack()

        food_submit = Button(self, bd=10, text='Search', command=lambda: self.api_search(food_var.get()))
        food_submit.pack()

        self.food_choices = Listbox(self, height=10, listvariable=self.api_list)
        self.food_choices.pack()

        print(type(self.api_list.get()))
        food_choice_sub = Button(self, bd=10, text='Yum!!',
                                 command=lambda: self.nutrition_info(self.food_choices.get(ANCHOR)[1]))
        food_choice_sub.pack()

    def api_search(self, search_param):

        print(search_param)
        payload = {'api_key': self.key, 'query': search_param}
        response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=payload)
        data = response.json()
        # keys = ['fdcId', 'description', 'dataType', 'brandOwner']
        #
        #
        for item in data:
            print(item)
            self.data_names.append(data)
        # for item in data:
        #
        #     # if len(item['description']) > len(search_param):
        #     #     print('might not be what I am looking for')
        #     #     print(item['description'])
        #     # else:
        #     #     self.data_names.append((item['description'], item['fdcId']))

        self.api_list.set(self.data_names)

    def nutrition_info(self, fcdid):

        payload = {'api_key': self.key}
        response = requests.get(f"https://api.nal.usda.gov/fdc/v1/food/{fcdid}", params=payload)
        data = response.json()

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
    window = Window()
    window.mainloop()

