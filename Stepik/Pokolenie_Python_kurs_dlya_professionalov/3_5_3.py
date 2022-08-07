
from datetime import date, time, datetime, timedelta


week = {0: ('9:00', '21:00'),
        1: ('9:00', '21:00'),
        2: ('9:00', '21:00'),
        3: ('9:00', '21:00'),
        4: ('9:00', '21:00'),
        5: ('10:00', '18:00'),
        6: ('10:00', '18:00')
        }

s = input().split()
my_date = datetime.strptime(s[0], '%d.%m.%Y').weekday()
my_time = datetime.strptime(s[1], '%H:%M')

if datetime.strptime(week[my_date][0], '%H:%M') <= my_time < datetime.strptime(week[my_date][1], '%H:%M'):
    print((datetime.strptime(week[my_date][1], '%H:%M') - my_time).seconds // 60)
else:
    print('Магазин не работает')
