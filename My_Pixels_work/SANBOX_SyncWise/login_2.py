import requests
import json
import create_signature
from create_signature_class import SyncwiseAPI


# api = SyncwiseAPI("https://dev-api.syncwise360.com")


class SyncwiseClient(SyncwiseAPI):
    SECRET_KEY = None
    def user_account_login(self):
        """
        Login user and get secret key
        """
        # url = f"https://dev-api.syncwise360.com/rest/action/{api.create_url_test_with_public()}"
        url = f"https://dev-api.syncwise360.com/rest/action/{self.create_url_test_with_public()}"

        payload = json.dumps({
            "username": "igorperetssuperior",
            "password": "1234"
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'https://sandbox.syncwise360.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        print(response.text)
        # print(response_data['secretKey'])
        self.SECRET_KEY = response_data['secretKey']

# PRIVATE
# # url = f"https://dev-api.syncwise360.com/rest/action/{create_signature.create_url_test_with_private(response_data['secretKey'])}"
# url = f"https://dev-api.syncwise360.com/rest/action/{api.create_url_test_with_private(response_data['secretKey'])}"
#
# payload = json.dumps({
#   "id_company": 2973,
#   "active": 1
# })
# headers = {
#   'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#   'sec-ch-ua-mobile': '?0',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
#   'Content-Type': 'application/json',
#   'Accept': '*/*',
#   'Referer': 'https://sandbox.syncwise360.com/',
#   'x-access-token': '72Y8ItBOOQT2S2u41cosMWw_hSjrpOreSND8N9iRaoO1B3k3wmUPA7dxt3yb',
#   'sec-ch-ua-platform': '"Windows"'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
# data = response.json()
#
# poligone_list = []
#
# for i in data['resultList']:
#     poligone_list.append(i['points'])
#
# print(poligone_list)


# CREATE GEOFENCE

test_1 = SyncwiseClient("https://dev-api.syncwise360.com")
test_1.user_account_login()
print(test_1.SECRET_KEY)
