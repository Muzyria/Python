import calendar


year, month = input().split()
print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])
