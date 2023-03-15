from datetime import datetime, timedelta

time_str = '17:58'
time_obj = datetime.strptime(time_str, '%H:%M')
new_time_obj = time_obj + timedelta(minutes=5)
new_time_str = new_time_obj.strftime('%H:%M')
print(new_time_str)  # '17:13'