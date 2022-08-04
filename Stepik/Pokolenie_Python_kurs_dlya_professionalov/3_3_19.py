from datetime import datetime


def is_available_date(booked_dates, date_for_booking):
    s = []
    for i in booked_dates:
        if len(i) == 10:
            s.append(datetime.strptime(i, "%d.%m.%Y").toordinal())
        else:
            s.extend([j for j in range(datetime.strptime(i.split("-")[0], "%d.%m.%Y").toordinal(),
                                       datetime.strptime(i.split("-")[1], "%d.%m.%Y").toordinal() + 1)])
    s = set(s)

    s2 = []
    if len(date_for_booking) == 10:
        s2.append(datetime.strptime(date_for_booking, "%d.%m.%Y").toordinal())
    else:
        s2.extend([j for j in range(datetime.strptime(date_for_booking.split("-")[0], "%d.%m.%Y").toordinal(),
                                    datetime.strptime(date_for_booking.split("-")[1], "%d.%m.%Y").toordinal() + 1)])
    s2 = set(s2)

    return s.isdisjoint(s2)


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
