import calendar


year, month = map(int, input().split())
print(calendar.monthrange(year, month)[1])
