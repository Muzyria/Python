
from datetime import datetime, timedelta


def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    lst_date = [datetime.strptime(i, pattern) for i in dates]
    start = sorted(lst_date)[0].date()
    end = sorted(lst_date)[-1].date()
    return [datetime.fromordinal(i).strftime(pattern) for i in range(start.toordinal(), end.toordinal() + 1)]


# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = [datetime.strptime(d, pattern) for d in dates]
#     start, end = min(dates), max(dates)
#     days = (end - start).days
#     return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))

dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))  # 304
print(fill_up_missing_dates(dates))

dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))  # 549
print(fill_up_missing_dates(dates))