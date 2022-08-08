
from datetime import timedelta, datetime


def choose_plural(amount: int, declensions: tuple) -> str:
    if amount % 10 in (0, 5, 6, 7, 8, 9) or amount % 100 in (11, 12, 13, 14):
        return declensions[2]
    elif amount % 10 == 1:
        return declensions[0]
    return declensions[1]


if __name__ == '__main__':
    course_date = datetime(day=8, month=11, year=2022, hour=12)
    str_day = ('день', 'дня', 'дней')
    str_hour = ('час', 'часа', 'часов')
    str_minute = ('минута', 'минуты', 'минут')
    pattern = '%d.%m.%Y %H:%M'
    my_date = datetime.strptime(input(), pattern)
    if my_date >= course_date:
        print('Курс уже вышел!')
    else:
        result = course_date - my_date
        days = result.days
        hours = result.seconds // 3600
        minutes = result.seconds // 60 % 60
        if days and hours:
            print(
                f'До выхода курса осталось: {days} {choose_plural(days, str_day)} и {hours} {choose_plural(hours, str_hour)}')
        if days and hours == 0:
            print(f'До выхода курса осталось: {days} {choose_plural(days, str_day)}')
        if days == 0 and hours and minutes:
            print(f'До выхода курса осталось: {hours} {choose_plural(hours, str_hour)} и {minutes} {choose_plural(minutes, str_minute)}')
        if days == 0 and hours == 0 and minutes:
            print(f'До выхода курса осталось: {minutes} {choose_plural(minutes, str_minute)}')
        if days == 0 and  minutes == 0 and hours:
            print(f'До выхода курса осталось: {hours} {choose_plural(hours, str_hour)}')
