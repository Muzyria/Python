
import requests
import json

url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceCreate/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/rtkqUdzocQGliPvE-Eauo_WbYelD1JkUFPOke5rLYYY/231030171715+0200/JSON"

payload = json.dumps({
  "active": 1,
  "status": 1,
  "visible": 1,
  "id_company": 2973,
  "id_geofenceType": 18,
  "points": [
    {
      "lat": 50.08094180506528,
      "lng": 36.231000423431404
    },
    {
      "lat": 50.081014094836945,
      "lng": 36.231939196586616
    },
    {
      "lat": 50.08059412416432,
      "lng": 36.23139202594758
    }
  ],
  "name": "cpo 18 hole",
  "geo_fence_type": "cart_path",
  "id_coursecheckpoint": "3190"
})
headers = {
  'authority': 'dev-api.syncwise360.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'content-type': 'application/json',
  'origin': 'https://sandbox.syncwise360.com',
  'referer': 'https://sandbox.syncwise360.com/',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  'x-access-token': 'NvOzltkl8f7AlxbxHARoV1cNOBAPYrd4CDi2xCpn6sHVLAnqj0UIFKplWJKy'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
