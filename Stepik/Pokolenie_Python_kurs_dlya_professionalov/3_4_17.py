
from datetime import timedelta, datetime

my_time = datetime.strptime(input(), '%H:%M:%S')
my_second = int(input())

print((my_time + timedelta(seconds=my_second)).strftime('%H:%M:%S'))
