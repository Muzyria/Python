
from datetime import date, timedelta

result = date(*map(int, input().split())) + timedelta(days=int(input()))
print(result.year, result.month, result.day)
