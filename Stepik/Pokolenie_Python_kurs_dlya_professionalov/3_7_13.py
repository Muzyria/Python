import calendar
from datetime import date, timedelta


def get_all_mondays(year):
    lst = []
    start_date = date(year, 1, 1)
    while start_date.year == year:
        if start_date.weekday() == 0:
            lst.append(start_date)
        start_date += timedelta(days=1)
    return lst


get_all_mondays(2021)


# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays