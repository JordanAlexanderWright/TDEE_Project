information = {
        '12/1/2021': {'Steak': {'Protein': 30, 'Calories': 500},
                     'Chicken': {'Protein': 30, 'Calories': 300}},
}


simple_dict = {
    'Steak': "Good",
    'Chicken': "Bad"
}


another_dict = {'Steak': {'Protein': 30, 'Calories': 500},
                'Chicken': {'Protein': 30, 'Calories': 300}}


# for key, value in information['12/1/2021']:
#     print(key)
#     for values in value:
#         print(value)

# for key, value in simple_dict.items():
#     print(key)
#     print(value)
#
# for thing in simple_dict.items():
#     print(thing)
#
# # information['12/1/2021'][key][key][value]
#
# info_text = []
#
# try_again = []
# for key in information['12/1/2021'].keys():
#     try_again.append((f"{key}: {information['12/1/2021'][key].items()}"))
#     for item in information['12/1/2021'][key].items():
#         info_text.append(f"{key}, {item[0]} {item[1]}")
#
# print(info_text)
# print(try_again)
#

print(another_dict)

somelist= []

for key in another_dict.keys():
    for thing in another_dict[key].items():
        print(f"{key}, {thing}")


# print(another_dict["Steak"].items())
#
# for thing in another_dict["Steak"].items():
#     print(thing)


