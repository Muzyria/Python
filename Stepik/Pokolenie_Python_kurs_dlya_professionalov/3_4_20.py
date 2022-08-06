
from datetime import datetime

pattern = '%d.%m.%Y'
lst_date = [datetime.strptime(i, pattern) for i in input().split()]
print([abs((lst_date[i] - lst_date[i-1]).days) for i in range(1, len(lst_date))])
