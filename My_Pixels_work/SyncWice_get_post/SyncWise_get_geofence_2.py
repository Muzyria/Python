import requests

class TestNew:
    def __init__(self):
        self.id_user = None
        self.secret_key = None
        self.ntest_post_authorization()

    def ntest_post_authorization(self):
        base_url = "https://dev-api.syncwise360.com/"
        resource = "rest/action/UserAccountLogin/FVyzsVqr-BmP280/1.0/2.0/HmacSHA256/3tamNhltdzlWTuaMg6ndCRzwa8o9aR2peFRkqAqP-w0/230227121909+0200/JSON"
        post_url = base_url + resource

        json_data = {"username": "igorperetssuperior", "password": "1234"}

        response = requests.post(post_url, json=json_data)

        assert response.status_code == 200, f"Expected 200 status code but received {response.status_code}"

        # print(response.content)
        self.secret_key = response.json()["secretKey"]
        print("Authorization successful")


    def ntest_get_geofence_list(self):
        url = 'https://dev-api.syncwise360.com/rest/action/CourseGeofenceList/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/' \
              'HmacSHA256/sDuRC0E2spuhh5XhIT6YXnW1Rjs8GCFMIE_CGp5j0Ts/230227121247+0200/JSON'
        params = {"id_course":"xqrRgFzOAmmP","id_company":2973,"active":1}
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': f'user_id=305; secretKey={self.secret_key}; apiKey=igolfsaltcreek',
            'Referer': 'https://accounts.syncwise360.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.post(url, params=params, headers=headers, verify=False)

        if response.status_code == 200:
            data = response.json()
            # обрабатываем полученные данные
        else:
            print(f'Request failed with status code {response.status_code}')

        print(self.secret_key)

new = TestNew()
print(new.secret_key)


# print(new.my_sesion.__dict__)
# new.ntest_get_geofence_list()
