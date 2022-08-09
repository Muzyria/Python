import calendar


date_in = input().split()
print(calendar.month(int(date_in[0]), list(calendar.month_abbr).index(date_in[1])))


# from calendar import prmonth
# from datetime import datetime
#
# dt = datetime.strptime(input() + ' 1', '%Y %b %d')
#
# prmonth(dt.year, dt.month)
