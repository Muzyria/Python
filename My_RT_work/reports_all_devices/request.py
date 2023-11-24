
import requests
import json


def login():
    url = "https://auth-direct-dev.hasgas.com.ua/auth/login"

    payload = json.dumps({
        "login": "MainAdminDirect",
        "password": "6AQyk4nDaI4"
    })
    headers = {
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Referer': 'https://direct-dev.hasgas.com.ua/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()['access']


def get_report(ser_num, ch_num, mf_num, type_dev, token, kgs='false', kkorr='false'):
    url = f"https://rest-direct-dev.hasgas.com.ua/api/v1/report?from=2023-10-01&to=2023-10-31&ksg={kgs}&kkorr={kkorr}"

    payload = json.dumps([
      {
        "serNUM": ser_num,
        "chNUM": ch_num,
        "mfDEV": mf_num,
        "typeDEV": type_dev
      }
    ])
    headers = {
      'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'Authorization': f'Bearer {token}',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/plain, */*',
      'Referer': 'https://direct-dev.hasgas.com.ua/',
      'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(rf'{response.text}')


# get_report()
# print(login())
