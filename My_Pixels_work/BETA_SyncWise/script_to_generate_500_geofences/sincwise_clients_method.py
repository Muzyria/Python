import time
import random

import requests
import json

from create_signature_class import SyncwiseAPI


# api = SyncwiseAPI("https://dev-api.syncwise360.com")


class SyncwiseClient(SyncwiseAPI):
    SECRET_KEY = None
    COURSE_GEOFENCE_LIST = None
    #
    COURSE_VECTOR_DETAILS = None
    COURSE_VECTOR_DETAILS_HOLECOUNT = None
    COURSE_VECTOR_DETAILS_CLUBHOUSE = {}
    COURSE_VECTOR_DETAILS_BACKGROUND = {}

    COURSE_VECTOR_DETAILS_HOLES = None
    COURSE_VECTOR_DETAILS_HOLES_PERIMETR = {}  # Special format for CREATE GEOFENCE - perimetr
    COURSE_VECTOR_DETAILS_HOLES_GREEN = {}  # Special format for CREATE GEOFENCE - green
    COURSE_VECTOR_DETAILS_HOLES_GREENCENTER = {}  # Special format for CREATE GEOFENCE - greencenter
    #
    COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH = {}  # Special format for DEVICE GET or SENS COORDINATES - centralpatch


    # PUBLIC
    def user_account_login(self):
        """
        Login user and get secret key
        """
        url = f"{self.host}/rest/action/{self.create_url_test_with_public()}"

        payload = json.dumps({
            "username": "igorperetssuperior",
            "password": "Qwerty01!"
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        print(response.text)
        self.SECRET_KEY = response_data['secretKey']

    # PRIVATE
    def course_geofence_list(self):
        """
        Get course geofence list
        """
        action = "CourseGeofenceList"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_company": 4442,
            "active": 1
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-access-token': '_dHjFdUbm5db7AibFL6fqYVpig1Wb0CyKeryH2YeN7sx2mGg056vEu2MbhkB'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.COURSE_GEOFENCE_LIST = data

        # print(self.COURSE_GEOFENCE_LIST)

        # poligone_list = []
        #
        # for i in data['resultList']:
        #     poligone_list.append(i['points'])
        #
        # print(poligone_list)

    def course_vector_details(self):
        """
        Get course vector details
        """
        action = "CourseVectorDetails"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_course": "KoyhA-zWt6os"
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-access-token': 'Wrle2mPGpJxOjyVztlCvGVpObNGfJT_xOoiMzRtd1b_eBCIkNBVsemMRGX9f'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.COURSE_VECTOR_DETAILS = data
        self.COURSE_VECTOR_DETAILS_HOLECOUNT = data['geometry']['HoleCount']
        self.COURSE_VECTOR_DETAILS_HOLES = data['geometry']['Holes']['Hole']

        # Write data for hole shape clubhouse
        point_str = data['geometry']['Clubhouse']['Shapes']['Shape'][0]['Points']
        self.COURSE_VECTOR_DETAILS_CLUBHOUSE[1] = [
            {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole shape background
        point_str = data['geometry']['Background']['Shapes']['Shape'][0]['Points']
        self.COURSE_VECTOR_DETAILS_BACKGROUND[1] = [
            {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole shape perimeter
        for item in range(self.COURSE_VECTOR_DETAILS_HOLECOUNT):
            point_str = self.COURSE_VECTOR_DETAILS_HOLES[item]['Perimeter']['Shapes']['Shape'][0]['Points']
            self.COURSE_VECTOR_DETAILS_HOLES_PERIMETR[item + 1] = [
                {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole shape green
        for item in range(self.COURSE_VECTOR_DETAILS_HOLECOUNT):
            point_str = self.COURSE_VECTOR_DETAILS_HOLES[item]['Green']['Shapes']['Shape'][0]['Points']
            self.COURSE_VECTOR_DETAILS_HOLES_GREEN[item + 1] = [
                {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole shape green
        for item in range(self.COURSE_VECTOR_DETAILS_HOLECOUNT):
            point_str = self.COURSE_VECTOR_DETAILS_HOLES[item]['Greencenter']['Shapes']['Shape'][0]['Points']
            self.COURSE_VECTOR_DETAILS_HOLES_GREENCENTER[item + 1] = [
                {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole centralPATH
        for item in range(self.COURSE_VECTOR_DETAILS_HOLECOUNT):
            point_str = self.COURSE_VECTOR_DETAILS_HOLES[item]['Centralpath']['Shapes']['Shape'][0]['Points']
            self.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[item + 1] = [
                {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

    def course_geofence_create(self, name, coordinates):
        """
        Create course geofence
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_company": 4442,
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
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-access-token': '_dHjFdUbm5db7AibFL6fqYVpig1Wb0CyKeryH2YeN7sx2mGg056vEu2MbhkB'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def course_geofence_CPO_create(self, name, coordinates, id_coursecheckpoint):
        # url = "https://api2.syncwise360.com/rest/action/CourseGeofenceCreate/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/VfqKqJXHt_nPX4QJL9rDztyJmbNaogBx5d44y89PvYQ/230831150147+0300/JSON"

        """
        Create course CPO geofence
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_company": 4442,
            "id_geofenceType": 18,
            "points": coordinates,
            "name": name,
            "geo_fence_type": "cart_path",
            "id_coursecheckpoint": id_coursecheckpoint  #"8952"  # this is first hole now
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-access-token': 'gd3OxaAYgtaFv9F2sOXF2aH92IIhzAR-Ena11N0b0PY1IbGQXwiFk4x4_miq'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)



    def move_geofence_to_square(self, geofence, target_square_center):
        # Вычислить смещение (разницу) между центрами
        lat_offset = target_square_center["lat"] - (geofence[0]["lat"] + geofence[1]["lat"] + geofence[2]["lat"]) / 3
        lng_offset = target_square_center["lng"] - (geofence[0]["lng"] + geofence[1]["lng"] + geofence[2]["lng"]) / 3

        # Применить смещение ко всем точкам геофенса
        moved_geofence = [
            {"lat": point["lat"] + lat_offset, "lng": point["lng"] + lng_offset}
            for point in geofence
        ]

        return moved_geofence

    def generate_random_target_square(self, min_lat, max_lat, min_lng, max_lng):
        random_lat = random.uniform(min_lat, max_lat)
        random_lng = random.uniform(min_lng, max_lng)
        return {"lat": random_lat, "lng": random_lng}

    def course_geofence_advertisement_type_create(self, name, coordinates=None):
        """
        Create course geofence advertisement type
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = {
            'request': json.dumps({
                "fileType": "image/jpeg",
                "companyCode": "DDg2_tDaqpk7",
                "active": 1,
                "id_company": 4442,
                "geofenceStatus": 1,
                "visible": 1,
                "id_geofenceType": 17,
                "marshallBypass": 1,
                "disabilityBypass": 0,
                "name": name,
                "points": coordinates
            }),
        }

        files = [('file', ('image.jpg', open('image.jpg', 'rb'), 'image/jpeg'))]

        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
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


    def course_geofence_advertisement_type_turn_off(self, id_geofence):
        # url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceUpdate/FVyzsVqr-BmP280/QA/1.0/2.0/HmacSHA256/jfC2MNAcNijykJPGY9Bytb_ZZEgS_tt_9k2EXFy3zF0/230830155134+0300/JSON"

        action = "CourseGeofenceUpdate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "status": 0
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-access-token': '_dHjFdUbm5db7AibFL6fqYVpig1Wb0CyKeryH2YeN7sx2mGg056vEu2MbhkB'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def course_geofence_advertisement_type_delete(self, id_geofence):
        # url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceUpdate/FVyzsVqr-BmP280/QA/1.0/2.0/HmacSHA256/dXKNzzJzuWDgVFBTwgCo2fAx_sVfHa5Op_PPLRbF9uo/230831123505+0300/JSON"

        action = "CourseGeofenceUpdate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "active": 0
        })
        headers = {
            'authority': 'api2.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://beta.syncwise360.com',
            'referer': 'https://beta.syncwise360.com/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-access-token': '_dHjFdUbm5db7AibFL6fqYVpig1Wb0CyKeryH2YeN7sx2mGg056vEu2MbhkB'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)





test_1 = SyncwiseClient("https://api2.syncwise360.com")
test_1.user_account_login()

print(test_1.SECRET_KEY)

# test_1.course_geofence_list()
# print(test_1.COURSE_GEOFENCE_LIST)
# print(test_1.COURSE_GEOFENCE_LIST["resultList"])


# for item in test_1.COURSE_GEOFENCE_LIST["resultList"]:
#     if item["id_geofenceType"] == 10 and "regular_type" in item["name"]:
#         print(f'{item["name"]} {item["id_geofence"]}')


# adv_list = [item["id_geofence"] for item in test_1.COURSE_GEOFENCE_LIST["resultList"] if item["id_geofenceType"] == 10 and "regular_type" in item["name"]]
# adv_list = [item["id_geofence"] for item in test_1.COURSE_GEOFENCE_LIST["resultList"] if item["id_geofenceType"] == 17]
#     # if item["id_geofenceType"] == 17:
#     #     print(f'{item["name"]} {item["id_geofence"]}')
#
# print(adv_list)
# print(len(adv_list))
#
# for i in adv_list:
#     test_1.course_geofence_advertisement_type_delete(i)


#
# test_1.course_vector_details()


# print(test_1.COURSE_VECTOR_DETAILS)
# print(test_1.COURSE_VECTOR_DETAILS_HOLES_PERIMETR)

# for k, v in test_1.COURSE_VECTOR_DETAILS_HOLES_PERIMETR.items():  # Create shape geofence
#     test_1.course_geofence_create(f"a_shape_{k}", test_1.COURSE_VECTOR_DETAILS_HOLES_PERIMETR[k])
#     print(f"CREATE GEOFENCE - {k}")
#     time.sleep(10)

# for k, v in test_1.COURSE_VECTOR_DETAILS_CLUBHOUSE.items():
#     print(k, v, len(v))

# print(test_1.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)

# test_1.course_geofence_create('Back_ground', test_1.COURSE_VECTOR_DETAILS_BACKGROUND[1])


min_square_lat = 50.08022234377751
max_square_lat = 50.09313658004037

min_square_lng = 36.24363899230958
max_square_lng = 36.25930309295655


geofence = [
  {
    "lat": 50.090761888323954,
    "lng": 36.24425053596497
  },
  {
    "lat": 50.091006246091446,
    "lng": 36.24435245990754
  },
  {
    "lat": 50.090834163286345,
    "lng": 36.24464213848115
  }
]




# for number in range(0, 3):
#     # Генерировать случайный центр в заданных границах квадрата
#     random_target_square = test_1.generate_random_target_square(min_square_lat, max_square_lat, min_square_lng, max_square_lng)
#     # Переместить геофенс в случайный квадрат
#     moved_geofence = test_1.move_geofence_to_square(geofence, random_target_square)
#     # test_1.course_geofence_advertisement_type_create(f"adv_type_{number}", moved_geofence)
#     test_1.course_geofence_CPO_create(f"CPO_type_{number}", moved_geofence)
#     # test_1.course_geofence_create(f"regular_type_{number}", moved_geofence)
#     print(f"GEOFENCE --- {number} CREATED")

for number in range(13):

    id_coursecheckpoint = 8952 + number
    for _ in range(0, 3):
        # Генерировать случайный центр в заданных границах квадрата
        random_target_square = test_1.generate_random_target_square(min_square_lat, max_square_lat, min_square_lng, max_square_lng)
        # Переместить геофенс в случайный квадрат
        moved_geofence = test_1.move_geofence_to_square(geofence, random_target_square)
        test_1.course_geofence_CPO_create(f"CPO_type_{number}", moved_geofence, id_coursecheckpoint)
        print(f"GEOFENCE --- {number} CREATED")