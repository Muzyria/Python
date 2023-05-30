import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL для запроса
url = 'https://redmine.syncwise.com/activity.atom?key=6bbaa888a50f02f885083ab2f56d584acfc1d0aa&user_id=359'

# Отправка GET-запроса и получение XML-ответа
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    xml_data = response.content

    # Создание объекта BeautifulSoup для парсинга XML
    soup = BeautifulSoup(xml_data, 'xml')

    # Извлечение информации за сегодня
    today = datetime.now().date()
    entries = soup.find_all('entry')
    for entry in entries:
        updated = entry.find('updated').text
        updated_date = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%SZ").date()
        if updated_date == today:
            title = __import__('re').search(r'#(\d+)', entry.find('title').text)[0]
            author = entry.find('author').text
            print(title)
            # print('Updated:', updated)
            # print('Author:', author)
            # print('---')

else:
    print('Ошибка при получении данных:', response.status_code)
