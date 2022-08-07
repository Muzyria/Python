
from datetime import date, time, datetime, timedelta

count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

pattern = '%d.%m.%Y'
start = datetime.strptime("01.01.0001", pattern)
end = datetime.strptime("31.12.9999", pattern)

for i in range(start.toordinal(), end.toordinal() + 1):
    day = datetime.fromordinal(i).day
    week_day = datetime.fromordinal(i).weekday()
    if day == 13:
        count[week_day] += 1

for i in count.values():
    print(i)


