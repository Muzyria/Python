from datetime import datetime

flag = True
pattern = '%d.%m.%Y'
n = int(input())
employees = {}
for _ in range(n):
    name, old = input().rsplit(" ", 1)
    employees.setdefault(datetime.strptime(old, pattern), []).append(name)

for k, v in sorted(employees.items()):
    if len(v) > 1:
        print(datetime.strftime(k, pattern))
        flag = False

if flag:
    print(*[datetime.strftime(k, pattern) for k, v in sorted(employees.items())], sep="\n")
