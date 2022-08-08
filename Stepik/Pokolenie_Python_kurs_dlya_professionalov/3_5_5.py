from datetime import datetime


n = int(input())
pattern = '%d.%m.%Y'
employees = []
for _ in range(n):
    name, old = input().rsplit(" ", 1)
    employees.append((datetime.strptime(old, pattern), name))

oldest = min(employees, key=lambda x: x[0])
lst_oldest = [i for i in employees if i[0] == oldest[0]]

if len(lst_oldest) == 1:
    print(lst_oldest[0][0].strftime(pattern), lst_oldest[0][1])
else:
    print(lst_oldest[0][0].strftime(pattern), len(lst_oldest))
