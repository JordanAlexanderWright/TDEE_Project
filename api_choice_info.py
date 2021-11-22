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

print(response.status_code)


working_with = response.json()

print(working_with['servingSize'])
print(working_with['labelNutrients'])

# food_id = 2165595