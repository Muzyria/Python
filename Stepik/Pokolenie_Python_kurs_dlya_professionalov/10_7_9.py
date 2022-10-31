from datetime import date


def years_days(year):
    start, end = date.toordinal(date(year, 1, 1)), date.toordinal(date(year, 12, 31))
    return (date.fromordinal(i) for i in range(start, end + 1))


dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
