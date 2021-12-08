import pickle

some_string = "I don't know why, but I am creating a sentence."
another_string = "I don't know why, but I am an idiot"

information = {
    "Date": 2021-3-20,
    "Steak": {
        "Protein": 30,
        "Calories": 500,
    },
    "Pizza": {
        "Protein": 20,
        "Calories": 750,
    }
}


information = {
    '12/1/2021': {'Steak': {'Protein': 30, 'Calories': 500},
                  'Chicken': {'Protein': 30, 'Calories': 300}},
    '12/2/2021': {'Pizza': {'Protein': 10, 'Calories': 400},
                  'Ice Cream': {'Calories': 800}},
}

new_info = {
    '12/3/2021': {'Poop': {'Protein': 40, 'Death': 'Imminent'}}
}
the_strings = (some_string, another_string)

# with open('data.pickle', 'wb') as file:
#     pickle.dump(information, file, pickle.HIGHEST_PROTOCOL)
#
#
# with (open("data.pickle", "rb")) as openfile:
#     data = pickle.load(openfile)
#     # print(data)
#     # print(data["Steak"])
#     for key in data.keys():
#         print(key)
#     for value in data.values():
#         print(value)

with(open("data.pickle", 'ab+')) as openfile:

    openfile.seek(0, 0)
    data = pickle.load(openfile)
    data.update(new_info)

    openfile.seek(0, 0)
    pickle.dump(data, openfile, pickle.HIGHEST_PROTOCOL)

    openfile.seek(0, 0)
    data = pickle.load(openfile)

    for key in data.keys():
        print(key)

# with(open("data.pickle", 'ab')) as openfile:
#     pickle.dump(new_info, openfile, pickle.HIGHEST_PROTOCOL)
#
# with(open("data.pickle", 'rb')) as openfile:
#     data = pickle.load(openfile)
#     more_data = pickle.load(openfile)
#
#     for key in more_data.keys():
#         print(key)



