import requests

class TestNew:
    def __init__(self):
        self.id_user = None
        self.secret_key = None
        self.timestamp = None
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
        print(f"Secret_key {self.secret_key}")



    def ntest_get_geofence_list(self):
        import requests
        import json
        import hashlib
        import hmac
        import base64
        import time

        def calculate_signature(to_sign_str, sign_method, secret_key):
            """Вычисляет подпись для строки"""
            message = to_sign_str.encode('utf-8')
            key = secret_key.encode('utf-8')
            if sign_method == 'HmacSHA256':
                algorithm = hashlib.sha256
            else:
                raise ValueError(f'Неподдерживаемый метод подписи: {sign_method}')
            signature = hmac.new(key, message, algorithm).digest()
            signature_b64 = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
            return signature_b64

        def to_sign(action_id, app_api_key, api_key, api_version, sig_version, sig_method, response_format):
            """Создает строку для подписи"""
            timestamp_str = time.strftime('%y%m%d%H%M%S%z')
            params = [action_id, app_api_key, api_key, api_version, sig_version, sig_method, timestamp_str,
                      response_format]
            params_str = '/'.join(params)
            print(timestamp_str)
            self.timestamp = timestamp_str
            return params_str

        # Пример использования
        action_id = 'CourseGeofenceList'
        app_api_key = 'FVyzsVqr-BmP280'
        api_key = 'igorperetssuperior'
        api_version = '1.0'
        sig_version = '2.0'
        sig_method = 'HmacSHA256'
        response_format = 'JSON'
        secret_key = self.secret_key  # 'your_application_secret_key'

        to_sign_str = to_sign(action_id, app_api_key, api_key, api_version, sig_version, sig_method, response_format)
        signature_ = calculate_signature(to_sign_str, sig_method, secret_key)
        signature_and_timestamp = f'{signature_}/{self.timestamp}'
        # Добавьте полученную подпись в параметры запроса


        url = f"https://dev-api.syncwise360.com/rest/action/CourseGeofenceList/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/{signature_and_timestamp}/JSON"
        print(url)
        payload = json.dumps({
            "id_course": "xqrRgFzOAmmP",
            "id_company": 2973,
            "active": 1
        })
        headers = {
            'authority': 'dev-api.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://sandbox.syncwise360.com',
            'referer': 'https://sandbox.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'x-access-token': 'wKbhvngJncQs9lziCGjQz1yjAihaBTZ9buFPDOwZCBfATC9D70c_Ux86GkM6'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

new = TestNew()

new.ntest_get_geofence_list()
