import re
import sys


phone_pattern = r'\d{1,3}(-|\s)\d{1,3}\1\d{4,10}'
for line in sys.stdin:
    data = re.search(phone_pattern, line).group()
    li = list(map(str, data.split() if ' ' in data else data.split('-')))
    print(f'Код страны: {li[0]}, Код города: {li[1]}, Номер: {li[2]}')


# pattern = r"(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})"
# for number in map(str.rstrip, sys.stdin):
#     match = re.fullmatch(pattern, number)
#     groups = match.groupdict()
#     print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")

# pattern=r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})'
# for c in map(str.strip, sys.stdin):
#     country, city, number =search(pattern, c).group(1,3,4)
#     print(f'Код страны: {country}, Код города: {city}, Номер: {number}')


# 1 877 2638277
# 91-011-23413627