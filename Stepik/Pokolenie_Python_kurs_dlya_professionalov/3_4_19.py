
from datetime import timedelta, date, datetime

pattern = '%d.%m.%Y'
my_date = datetime.strptime(input(), pattern)

print(my_date.strftime(pattern))
for i in range(2, 11):
    my_date += timedelta(days=i)
    print(my_date.strftime(pattern))
