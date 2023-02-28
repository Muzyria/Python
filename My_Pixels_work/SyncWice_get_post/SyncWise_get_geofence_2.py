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
        import requests
        import json

        url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceList/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0" \
              "/HmacSHA256/yU-yL4fB2KmfbeOtu6bJ_AE7V6tmOJ9sNl4rQ4tM-DE/230228125424+0200/JSON"

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
            'x-access-token': '5tYD1C8LmsKE0qahys-q5YvHQF92iH0-ENzteFMtSSlLxZdUZ2-7Eicg3Scf'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

new = TestNew()
print(new.secret_key)


new.ntest_get_geofence_list()
