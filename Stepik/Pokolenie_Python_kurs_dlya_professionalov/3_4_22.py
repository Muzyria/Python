
from datetime import datetime, timedelta


pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

while start + timedelta(minutes=45) <= end:
    end_class = start + timedelta(minutes=45)
    print(f'{start.strftime(pattern)} - {end_class.strftime(pattern)}')
    start += timedelta(minutes=55)
