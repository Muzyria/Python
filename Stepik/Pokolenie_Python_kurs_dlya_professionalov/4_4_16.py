import json
with open('food_services.json', encoding='utf-8') as f1:
    data = list(json.load(f1))
types = dict()

for i in data:
    name, count = i["Name"], i["SeatsCount"]
    if i["TypeObject"] not in types:
        types[i["TypeObject"]] = (name, count)
    elif count > types[i["TypeObject"]][1]:
        types[i["TypeObject"]] = (name, count)

for k, v in sorted(types.items()):
    print(f'{k}: {v[0]}, {v[1]}')
