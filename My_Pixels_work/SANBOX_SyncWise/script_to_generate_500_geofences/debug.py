cord = [50.09299891996568, 36.24363899230958, 50.09313658004037, 36.25930309295655,50.0806629720677, 36.258916854858406, 50.08022234377751, 36.24402523040772]

print(sorted(cord))

import requests
import json

url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceUpdate/FVyzsVqr-BmP280/QA/1.0/2.0/HmacSHA256/jfC2MNAcNijykJPGY9Bytb_ZZEgS_tt_9k2EXFy3zF0/230830155134+0300/JSON"

payload = json.dumps({
  "id_geofence": 12136,
  "status": 0
})
headers = {
  'authority': 'dev-api.syncwise360.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'content-type': 'application/json',
  'origin': 'https://sandbox.syncwise360.com',
  'referer': 'https://sandbox.syncwise360.com/',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'x-access-token': 'mBH0N6fxP_Lnz8nCkNn8zH5w67VX7m8F_a_IHBotPJGrWAFiDf3B1YoObC_G'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
