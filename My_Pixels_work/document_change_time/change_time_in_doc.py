import re
from datetime import datetime, timedelta
from random import randrange


time_list = []


def change_time(value):
    time_str = value
    time_obj = datetime.strptime(time_str, '%H:%M')
    new_time_obj = time_obj + timedelta(hours=-0.5, minutes=randrange(1, 3))
    new_time_str = new_time_obj.strftime('%H:%M')
    # print(f'{value} -> {new_time_str}')
    time_list.append(new_time_str)
    return new_time_str


with open('text.txt', 'r', encoding='utf-8') as file:
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


def take_hour(start, finish):
    time1 = start
    time2 = finish
    # преобразуем временные метки в минуты
    hours1, minutes1 = map(int, time1.split(":"))
    hours2, minutes2 = map(int, time2.split(":"))
    total_minutes1 = hours1 * 60 + minutes1
    total_minutes2 = hours2 * 60 + minutes2
    # вычисляем разницу
    difference_hours = (total_minutes2 - total_minutes1) // 60
    difference_minutes = (total_minutes2 - total_minutes1) % 60
    # выводим результат
    print("Разница между временными метками: {} часов {} минут".format(difference_hours, difference_minutes))


print()
print(f'{min(time_list)} ---> {max(time_list)}')
take_hour(min(time_list), max(time_list))
