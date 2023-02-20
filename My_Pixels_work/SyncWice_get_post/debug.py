import requests

url = 'https://api-dna.igolf.com/rest/action/UserAccountLogin/uUqnXUKU86kghJk/1.0/2.0/HmacSHA256/2Wx7AIBZ4ctGrThUZVTWgvyq-qVGYz2NVDW9SbHQgyQ/221229151003GMT+02:00/JSON'
payload = {
    "username": "igolfsaltcreek",
    "password": "92108340"
}
response = requests.post(url, json=payload)

# выводим содержимое ответа в консоль
print(response.json())

# import requests

url = 'https://accounts.syncwise360.com/proxy_dna/CourseGeofenceList/?id_company=236&active=1'
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "user_id=305; secretKey=pZMmnOwBiihuk0tOGBbP3sEQHHswSjQe1ZsMfY-Zh_yKCmKUfm13EwRmJtpE; apiKey=igolfsaltcreek",
    "Referer": "https://accounts.syncwise360.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
response = requests.get(url, headers=headers)

# выводим содержимое ответа в консоль
print(response.json())

