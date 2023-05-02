from datetime import date

year, month = int(input()), int(input())

for i in range(1, 8):
    if date(year, month, i).isoweekday() == 4:
        day = i + 21

print(date(year, month, day).strftime('%d.%m.%Y'))
