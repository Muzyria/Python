import time

import requests
import json

from create_signature_class import SyncwiseAPI


# api = SyncwiseAPI("https://api2.syncwise360.com")


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

        # poligone_list = []
        #
        # for i in data['resultList']:
        #     poligone_list.append(i['points'])
        #
        # print(poligone_list)

    def course_vector_details(self, id_course):
        """
        Get course vector details
        """
        action = "CourseVectorDetails"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            # "id_course": "KoyhA-zWt6os"
            "id_course": id_course
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
            "id_geofenceActionType": 66,
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


# test_1 = SyncwiseClient("https://api2.syncwise360.com")
# test_1.user_account_login()
#
#
# print(test_1.SECRET_KEY)
#
# test_1.course_geofence_create('QWE5555', [
#     {
#       "lat": 50.09112670368736,
#       "lng": 36.23535633087159
#     },
#     {
#       "lat": 50.09242074333338,
#       "lng": 36.24127864837647
#     },
#     {
#       "lat": 50.09456822137395,
#       "lng": 36.23578548431397
#     }
#   ])



# test_1.course_geofence_list()
# print(test_1.COURSE_GEOFENCE_LIST)
#
# test_1.course_vector_details()
# print(test_1.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH)
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
