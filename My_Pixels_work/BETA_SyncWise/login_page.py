import requests
import json

url = "https://api2.syncwise360.com/rest/action/UserAccountLogin/FVyzsVqr-BmP280/1.0/2.0/HmacSHA256/mCreNCp6bbEJaTxJbwMMzakT8xF_xJETeugBilE-rb4/230602154652+0300/JSON"

payload = json.dumps({
  "username": "igorperetssuperior",
  "password": "1234"
})
headers = {
  'authority': 'api2.syncwise360.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'content-type': 'application/json',
  'origin': 'https://beta.syncwise360.com',
  'referer': 'https://beta.syncwise360.com/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.post(url, headers=headers, data=payload)
data = response.json()

print(data)


url = "https://api2.syncwise360.com/rest/action/CourseGeofenceList/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/230602163047+0300/JSON"

payload = json.dumps({
  "id_company": 4442,
  "active": 1
})
headers = {
  'authority': 'api2.syncwise360.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'content-type': 'application/json',
  'origin': 'https://beta.syncwise360.com',
  'referer': 'https://beta.syncwise360.com/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'x-access-token': f'{data["secretKey"]}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
