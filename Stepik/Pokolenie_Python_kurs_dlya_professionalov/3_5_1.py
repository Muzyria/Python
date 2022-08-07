from datetime import date, time, datetime, timedelta


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

pattern = '%H:%M'
count = 0

for i in data:
    s = datetime.strptime(i[1], pattern) - datetime.strptime(i[0], pattern)
    count += s.total_seconds() // 60

print(int(count))

# total = 0
# patern = '%H:%M'
# for my_date in data:
#         start, end = [datetime.strptime(d, patern) for d in my_date]
#         total += (end - start).seconds // 60
# print(total)