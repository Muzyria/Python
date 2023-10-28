cord = [50.09299891996568, 36.24363899230958, 50.09313658004037, 36.25930309295655,50.0806629720677, 36.258916854858406, 50.08022234377751, 36.24402523040772]

print(sorted(cord))





DICT_IP_DEVICES = {'W_W_W_->>>': '192.168.3.219'}

print(DICT_IP_DEVICES)

# def one(i):
#     def two():
#         print("two")
#
#     for _ in range(i):
#         two()
# one(5)

import requests
import json

url = "https://api2.syncwise360.com/rest/action/CourseGeofenceDetails/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/_Xl1-CugZPd7Irw5cI_mrn01yFgzLbgTwlyP2WQ2rrw/231028233121+0300/JSON"

payload = json.dumps({
  "id_geofence": 34391
})
headers = {
  'authority': 'api2.syncwise360.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'content-type': 'application/json',
  'origin': 'https://beta.syncwise360.com',
  'referer': 'https://beta.syncwise360.com/',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  'x-access-token': 'oHHw9yOaplcl7DQLCiAdIRDsoNJ2JWHEhgDluvlPrlZeLE1jSNXc4Sha_hnQ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
