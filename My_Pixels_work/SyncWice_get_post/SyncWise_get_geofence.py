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

        self.id_user = check_post['id_user']
        self.secretKey = check_post['secretKey']


    def ntest_get_geofence_list(self):
        base_url = "https://accounts.syncwise360.com/proxy_dna/CourseGeofenceList/?id_company=236&active=1"  # базовая url
        # result_get = requests.get(base_url, )


new = Test_new()
print(new.__dict__, "++++++++++++++++++++")
