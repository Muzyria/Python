from datetime import datetime, timedelta


from datetime import datetime, timedelta

if __name__ == '__main__':
    pattern = '%d.%m.%Y'
    my_date = datetime.strptime(input(), pattern)
    n = int(input())
    employees = []
    for _ in range(n):
        name, lastname, birthday = input().split()
        birthday = datetime.strptime(birthday, pattern)
        employees.append((name, lastname, birthday))
    my_dates = [(d.day, d.month) for d in (my_date + timedelta(i) for i in range(1, 8))]
    try:
        younger_employees = max(
            [employee for employee in employees if (employee[2].day, employee[2].month) in my_dates],
            key=lambda x: x[2])
        print(*younger_employees[:2])
    except ValueError:
        print('Дни рождения не планируются')
