
import requests

url = "https://accounts.syncwise360.com/proxy_dna/CourseGeofenceList/?id_company=236&active=1"

payload={}
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': 'user_id=305; secretKey=oaGKCU8QEh9UqhixQKUzyS9ZZcMqpZjD6xicdpA0Bob8yskPuBhlfmHYaiPn; apiKey=igolfsaltcreek',
  'Referer': 'https://accounts.syncwise360.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
