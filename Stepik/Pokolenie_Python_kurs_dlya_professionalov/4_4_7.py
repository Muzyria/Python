
import json


with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)                # передаем файловый объект
    lst = []
    for i in data:
        if type(i) == str:
            lst.append(i + '!')
        if type(i) == int:
            i += 1
            lst.append(i)
        if type(i) == bool:
            if i:
                i = False
            else:
                i = True
            lst.append(i)
        if type(i) == list:
            i = i * 2
            lst.append(i)
        if type(i) == dict:
            i["newkey"] = None
            lst.append(i)
        if i is None:
            continue

    with open('updated_data.json', 'w', encoding='utf=8') as file:
        json.dump(lst, file, indent=3)

print(lst)

# import json
#
#
# with open('data.json', 'r', encoding='utf8') as f:
#     data = json.load(f)
#
# res = []
# d = {
#     str: lambda x: x + '!',
#     int: lambda x: x + 1,
#     bool: lambda x: not x,
#     list: lambda x: x + x,
#     dict: lambda x: dict(list(x.items()) + [["newkey", None]])
# }
#
# for i in data:
#     if not (i is None):
#         res.append(d[type(i)](i))
#
# with open('updated_data.json', 'w', encoding='utf8') as res_file:
#     json.dump(res, res_file)