
import calendar

year, month, day = map(int, input().split('-'))

i = calendar.weekday(year, month, day)

print(list(calendar.day_name)[i])

# import calendar
# from datetime import datetime
#
# dt = datetime.fromisoformat(input())
#
# print(list(calendar.day_name)[dt.weekday()])
