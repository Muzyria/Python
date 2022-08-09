import calendar
from datetime import date


def get_days_in_month(year, month):
    days = calendar.monthrange(int(year), list(calendar.month_name).index(month))[1]
    month = list(calendar.month_name).index(month)
    lst_dates = [date(year, month, i) for i in range(1, days + 1)]
    return lst_dates


get_days_in_month(2021, 'December')
