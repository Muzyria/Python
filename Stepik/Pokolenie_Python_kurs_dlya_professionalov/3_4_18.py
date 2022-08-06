
from datetime import timedelta, date


def num_of_sundays(year):
    start = date(year, 1, 1)
    count = 0
    while start.year != year + 1:
        if start.weekday() == 6:
            count += 1
        start += timedelta(days=1)
    return count


print(num_of_sundays(2021))

year = 2000
print(num_of_sundays(year))
