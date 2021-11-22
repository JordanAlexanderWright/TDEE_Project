import requests

print("Please Input a food you'd like to lookup")
food = input()
my_key = 'WsAc8bOO00nv2sgDqa7PkIYHZtz2Utq8tKJHVuKS'
query_type = 'list'
payload = {'api_key': my_key, 'query': food}
response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list", params=payload)

print(response.status_code)

information = response.json()

# response.json() here creates a list of dictionaries.

for item in information:
    try:
        print(item['fdcId', 'description'])
    except KeyError:
        print("There may be an error")

# print(information)
#
#
# fdcId
# description
# dataType
# food_id = 2165595