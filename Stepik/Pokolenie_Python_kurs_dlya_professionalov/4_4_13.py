import json
from datetime import time

with open('pools.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    lst_pool = []
    for row in data:
        time_work_start, time_work_finish = row['WorkingHoursSummer']['Понедельник'].split('-')
        if time.fromisoformat(time_work_start) <= time(10) \
                and time.fromisoformat(time_work_finish) >= time(12):
            lst_pool.append([row["Address"], row['DimensionsSummer']['Length'], row['DimensionsSummer']['Width']])
    result = max(lst_pool, key=lambda x: (x[1], x[2]))
    print(f'{result[1]}x{result[2]}')
    print(result[0])
