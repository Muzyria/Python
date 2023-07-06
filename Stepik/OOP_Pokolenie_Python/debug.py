from datetime import datetime, timedelta

# Получаем текущую дату и время
current_datetime = datetime.now()


# Добавляем timedelta к текущей дате и времени
new_datetime = current_datetime + timedelta(minutes=0, seconds=-120)

print("Текущая дата и время:", current_datetime.strftime('%H:%M:%S'))
print("Новая дата и время:", new_datetime.strftime('%H:%M:%S'))
print(current_datetime < new_datetime)
print(datetime.now() > new_datetime)
