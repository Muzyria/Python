import requests

class Test_new:
    def __init__(self):
        self.id_user = None
        self.secretKey = None
        self.ntest_post_authorisaion()

    def ntest_post_authorisaion(self):
        base_url = "https://api-dna.igolf.com/rest/action/"  # базовая url
        post_resource = "UserAccountLogin/uUqnXUKU86kghJk/1.0/2.0/HmacSHA256/2Wx7AIBZ4ctGrThUZVTWgvyq-qVGYz2NVDW9SbHQgyQ/221229151003GMT+02:00/JSON"  # Ресурс метода пост
        post_url = base_url + post_resource
        print(post_url)

        json_post = {
                    "username": "igolfsaltcreek",
                    "password": "92108340"
                    }

        result_post = requests.post(post_url, json=json_post)

        assert 200 == result_post.status_code
        print("Успешно!!!")

        check_post = result_post.json()
        print(check_post)

        self.id_user = check_post['id_user']
        self.secretKey = check_post['secretKey']


    def ntest_get_geofence_list(self):
        url = 'https://accounts.syncwise360.com/proxy_dna/CourseGeofenceList/'
        params = {'id_company': '236', 'active': '1'}
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': f'user_id=305; secretKey={self.secretKey}; apiKey=igolfsaltcreek',
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

        response = requests.get(url, params=params, headers=headers, verify=False)

        if response.status_code == 200:
            data = response.json()
            # обрабатываем полученные данные
        else:
            print(f'Request failed with status code {response.status_code}')

        print(self.secretKey)
new = Test_new()
new.ntest_get_geofence_list()
