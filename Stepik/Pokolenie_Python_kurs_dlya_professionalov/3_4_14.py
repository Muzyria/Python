
from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = (timedelta(date.toordinal(birthday)) - timedelta(date.toordinal(today)))

print(days.days)
