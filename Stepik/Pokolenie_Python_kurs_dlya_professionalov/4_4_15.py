import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
