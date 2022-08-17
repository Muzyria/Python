import json

with open('people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    lst_key = set()
    for item in data:
        for key in item:
            lst_key.add(key)
    d = dict().fromkeys(lst_key, None)

    for i in range(len(data)):
        for key in d:
            if key not in data[i]:
                data[i][key] = None

    with open('updated_people.json', 'w', encoding='utf-8') as file_w:
        json.dump(data, file_w, indent=3)
