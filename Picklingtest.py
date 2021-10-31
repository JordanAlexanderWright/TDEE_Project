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

the_strings = (some_string, another_string)
#
# with open('data.pickle', 'wb') as file:
#     pickle.dump(information, file, pickle.HIGHEST_PROTOCOL)


with (open("data.pickle", "rb")) as openfile:
    data = pickle.load(openfile)
    print(data)
    print(data["Steak"])
    for key in data.values():
        print(key)


