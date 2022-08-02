
from datetime import date


def print_good_dates(args):
    if args:
        lst = [i for i in args if i.year == 1992 and i.day + i.month == 29]
        print(*list(i.strftime('%B %d, %Y') for i in sorted(lst)), sep="\n")


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
