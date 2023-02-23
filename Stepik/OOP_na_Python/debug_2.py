# import time
#
# import pyautogui
#
#
# while True:
#     x, y = pyautogui.position()
#     print(f"Текущие координаты курсора: x={x}, y={y}")
#     time.sleep(0.5)

import requests

# params = {"q": "funny cats"}
data = {
    "comments": "zzzzzzzzzzzzzzzzzzzzzzzzzzz",
    "custemail": "fila080@gmail.com",
    "custname": "Oleksandr",
    "custtel": "0933095250",
    "delivery": "18:15",
    "size": "small",
    "topping": "onion"
  }

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-63f77622-4c69deb85d40ee995ea899ac"
  }



variable = requests.Session()

variable.get("https://httpbin.org/form/post")

response = requests.post("https://httpbin.org/post", headers=headers, data=data)

# print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
print(response)



