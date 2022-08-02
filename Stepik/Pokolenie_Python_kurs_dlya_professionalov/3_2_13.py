# from datetime import date
#
#
# n = int(input())
# lst = [date.fromisoformat(input()) for _ in range(n)]
#
# [print(i.strftime('%d/%m/%Y')) for i in sorted(lst)]



# n = int(input())
# [print(i.strftime('%d/%m/%Y')) for i in sorted([date.fromisoformat(input()) for _ in range(n)])]

from datetime import date

[print(i.strftime('%d/%m/%Y')) for i in sorted([date.fromisoformat(input()) for _ in range(int(input()))])]
