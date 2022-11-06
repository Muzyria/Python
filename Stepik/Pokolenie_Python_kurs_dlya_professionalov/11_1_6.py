import re


s = 'Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911'

match = re.findall('7-\d\d\d-\d\d\d-\d\d-\d\d' or '8-\d\d\d-\d\d\d\d-\d\d\d\d', s)
print(match)
