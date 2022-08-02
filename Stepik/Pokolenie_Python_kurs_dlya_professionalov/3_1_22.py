from datetime import date


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    return len([date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)
                if date.fromordinal(i).weekday() == 5])


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
