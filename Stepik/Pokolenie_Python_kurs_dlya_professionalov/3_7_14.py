import calendar
from datetime import date


def third_thursday_of_the_month(year):
    pattern = '%d.%m.%Y'
    d_lst = {}
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            my_day = week[3]
            if my_day:
                d_lst.setdefault(month, []).append((date(year, month, my_day)).strftime(pattern))
        print(d_lst[month][2])
        d_lst = {}


third_thursday_of_the_month(int(input()))
