import certifi
import requests

url = 'https://accounts.syncwise360.com/proxy_dna/CourseGeofenceList/'
params = {'id_company': '236', 'active': '1'}
headers = {

    'Cookie': 'user_id=305; secretKey=vtx-RvqdAODfIeG3P8m4g4TKU175iT_sMsGG72t00hOVcFhn1og5xlCAfW1e; apiKey=igolfsaltcreek',
    'Referer': 'https://accounts.syncwise360.com/',

}

response = requests.get(url, params=params, headers=headers, verify=certifi.where())

if response.status_code == 200:
    data = response.json()
    # обрабатываем полученные данные
else:
    print(f'Request failed with status code {response.status_code}')

