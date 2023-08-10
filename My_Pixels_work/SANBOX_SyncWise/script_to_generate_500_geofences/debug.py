import requests

url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceCreate/FVyzsVqr-BmP280/qauatwincitydev/1.0/2.0/HmacSHA256/OJjFEG3PF_fXa9C-r5_qZ_QQXjU7wwwRbMiEqhrltIU/230810121940+0300/JSON"

payload = {'request': '{"fileType":"image/jpeg","companyCode":"lsQafn5n7DUK","active":1,"id_company":2325,"geofenceStatus":1,"visible":1,"id_geofenceType":17,"marshallBypass":1,"disabilityBypass":0,"name":"4444","points":[{"lat":32.95181966580096,"lng":-82.85081863403322},{"lat":32.951837671538215,"lng":-82.85045385360719},{"lat":32.9515135677063,"lng":-82.85062551498415}]}'}
files=[
  ('file',('image.jpg',open('/C:/Users/Fila0/Downloads/image.jpg','rb'),'image/jpeg'))
]
headers = {
  'authority': 'dev-api.syncwise360.com',
  'accept': 'application/json',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
  'origin': 'https://sandbox.syncwise360.com',
  'referer': 'https://sandbox.syncwise360.com/',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)





payload = {
    'request': json.dumps({
        "active": 1,
        "status": 1,
        "visible": 1,
        "id_company": 2973,
        "id_geofenceType": 10,
        "name": name,
        "marshallBypass": 1,
        "disabilityBypass": 1,
        "controlLevel": 22,
        "customShutdownTimeout": None,
        "customRestoreTimeout": None,
        "geo_fence_type": "cart_control",
        "id_geofenceActionType": 60,
        "points": coordinates,
        "defaultMessage": 1
    }),
    'file': ('image.jpg', open(r'ПУТЬ_К_ФАЙЛУ\image.jpg', 'rb'), 'image/jpeg')
}