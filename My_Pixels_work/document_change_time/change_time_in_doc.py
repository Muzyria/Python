import re
from datetime import datetime, timedelta
from random import randrange


def change_time(value):
    time_str = value
    time_obj = datetime.strptime(time_str, '%H:%M')
    new_time_obj = time_obj + timedelta(minutes=randrange(3, 5))
    new_time_str = new_time_obj.strftime('%H:%M')
    # print(f'{value} -> {new_time_str}')
    return new_time_str


with open('text.txt', 'r',encoding='utf-8') as file:
    with open('new_text.txt', 'w', encoding='utf8') as file_write:
        for i in file:
            res = re.findall(r'\d\d:\d\d', i)
            if res:
                res_2 = re.sub(r'\d\d:\d\d', change_time(res[0]), i)
                print(res_2.strip())
                file_write.write(res_2)
            else:
                print(i.strip())
                file_write.write(i)
