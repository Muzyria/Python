
import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))
print(is_correct_json('number = 17'))
