import json

with open('countries.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    result = {}
    for i in data:
        result.setdefault(i['religion'], []).append(i['country'])

    with open('religion.json', 'w', encoding='utf-8') as file_w:
        json.dump(result, file_w, indent=3)
