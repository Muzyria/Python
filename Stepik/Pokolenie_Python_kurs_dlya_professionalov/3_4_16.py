
from datetime import timedelta

hours, minutes, seconds = map(int, input().split(':'))
print(int(timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()))
