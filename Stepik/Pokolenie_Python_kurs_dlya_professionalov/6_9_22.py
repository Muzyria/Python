import json
from collections import Counter, ChainMap

total = 0
with open('zoo.json', 'r', encoding='utf-8') as file:
    rows = json.load(file)
    for row in rows:
        total += Counter(row).total()
    print(total)


# from collections import ChainMap, Counter
# import json
#
# with open('zoo.json', 'r', encoding='utf-8') as json_file:
#     print(Counter(ChainMap(*json.load(json_file))).total())
