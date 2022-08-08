
from datetime import date, time, datetime, timedelta

pattern = '%d.%m.%Y'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

for i in range(start.toordinal(), end.toordinal() + 1):
    s = (datetime.fromordinal(i).day + datetime.fromordinal(i).month)
    if s % 2 == 1:
        start = datetime.fromordinal(i)
        break

for i in range(start.toordinal(), end.toordinal() + 1, 3):
    if datetime.fromordinal(i).weekday() not in (0, 3):
        print(datetime.fromordinal(i).date().strftime(pattern))

# from datetime import timedelta, datetime
#
# if __name__ == '__main__':
#     pattern = '%d.%m.%Y'
#     start = datetime.strptime(input(), pattern)
#     end = datetime.strptime(input(), pattern)
#     while True:
#         if (start.day + start.month) % 2 == 0:
#             start += timedelta(days=1)
#         else:
#             break
#     while True:
#         if start.weekday() not in (0, 3):
#             print(start.strftime(pattern))
#         start += timedelta(days=3)
#         if start > end:
#             break
