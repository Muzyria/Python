
from datetime import date, timedelta, datetime

my_date = datetime.strptime(input(), '%d.%m.%Y')

print((my_date - timedelta(hours=24)).strftime('%d.%m.%Y'))
print((my_date + timedelta(hours=24)).strftime('%d.%m.%Y'))

# from datetime import datetime, timedelta
#
# pattern, td = '%d.%m.%Y', timedelta(days=1)
#
# dt = datetime.strptime(input(), pattern)
#
# print((dt - td).strftime(pattern))
# print((dt + td).strftime(pattern))
