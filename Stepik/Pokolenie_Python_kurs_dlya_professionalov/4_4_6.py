
import sys
import json

for k, v in json.loads(sys.stdin.read()).items():
    if type(v) == list:
        print(f'{k}: {", ".join(list(map(str, v)))}')
    else:
        print(f'{k}: {v}')


# {
# "src": "Images/Sun.png",
# "name": "sun1",
# "hOffset": 250,
# "AAA": ["ABC", 123, 123, "XYZ"],
# "vOffset": 250,
# "alignment": "center",
# "key": [1, 2, 3, 4, 5],
# "another_key": ["a", "b", "c"]
# }
