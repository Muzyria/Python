import re
from datetime import datetime, timedelta
from random import randrange


def change_time(value):
    time_str = value
    time_obj = datetime.strptime(time_str, '%H:%M')
    new_time_obj = time_obj + timedelta(minutes=randrange(2, 5))
    new_time_str = new_time_obj.strftime('%H:%M')
    print(f'{value} -> {new_time_str}')
    return new_time_str


with open('text.txt', 'r',encoding='utf-8') as file:
    for i in file:
        res = re.findall(r'\d\d:\d\d', i.strip())
        if res:
            change_time(res[0])
