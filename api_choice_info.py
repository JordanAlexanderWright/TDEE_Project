import requests

# print("Please Input a food you'd like to lookup")
# food = input()
food = 2165595
my_key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
# query_type = 'list'
# payload = {'api_key': my_key, 'query': food}
# response = requests.get("https://api.nal.usda.gov/fdc/v1/food/2165595", params=payload)

payload = {'api_key': my_key}
response = requests.get("https://api.nal.usda.gov/fdc/v1/food/2165595", params=payload)

# print(working_with['servingSize'])
# print(working_with['labelNutrients'])
# print(response.status_code)


payload = {'api_key': my_key, 'query': 'Chicken Strips', 'requireAllWords': True, 'pageSize': 5,
           'dataType': ['Branded']}

# dataType params can be 'Branded' and / or 'Survey(FNDDS)'
# Both Data Types have to be treated differently.
response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=payload)
data = response.json()

print(data.keys())

print(data['foodSearchCriteria'])
print(data['totalHits'])

print(data['foods'])


for food in data['foods']:
    print(f"{food['servingSize']}{food['servingSizeUnit']}")
    print(food['brandName'])

    # This syntax will get the serving size and unit and return it as a string.
    # for item in food:
    #     print(item)
    # print(food['fdcId'])
    # print(food['lowercaseDescription'])
