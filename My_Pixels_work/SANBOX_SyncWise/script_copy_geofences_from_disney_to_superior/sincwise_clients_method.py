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

    def __init__(self, host, url, username, password, id_company, id_course, company_code):
        super().__init__(host, username)  # Вызываем конструктор родительского класса
        self.url = url
        self.password = password
        self.id_company = id_company
        self.id_course = id_course
        self.company_code = company_code

    # PUBLIC
    def user_account_login(self):
        """
        Login user and get secret key
        """
        url = f"{self.host}/rest/action/{self.create_url_test_with_public()}"

        payload = json.dumps({
            "username": self.username,
            "password": self.password
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': self.url,
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
            "id_company": self.id_company,
            "active": 1
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': self.url,
            'x-access-token': '72Y8ItBOOQT2S2u41cosMWw_hSjrpOreSND8N9iRaoO1B3k3wmUPA7dxt3yb',
            'sec-ch-ua-platform': '"Windows"'
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

    # PRIVATE
    def course_geofence_details(self, id_geofence):
        """Get course geofence details"""
        action = "CourseGeofenceDetails"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_geofence": id_geofence
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-access-token': 'oHHw9yOaplcl7DQLCiAdIRDsoNJ2JWHEhgDluvlPrlZeLE1jSNXc4Sha_hnQ'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        data = response.json()
        return data

    # PRIVATE
    def course_vector_details(self):
        """
        Get course vector details
        """
        action = "CourseVectorDetails"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_course": self.id_course
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-access-token': 'bjVDR13m9pZq1wLRRlc2a-qNaqZDM2mbrv78Hnmx7oCZ1qO5hrhnk5AX9mTr'
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

    def course_geofence_create(self, name, coordinates, id_geofence_action_type=60):
        """
        Create course geofence
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_company": self.id_company,
            "id_geofenceType": 10,
            "name": name,
            "marshallBypass": 1,
            "disabilityBypass": 1,
            "controlLevel": 22,
            "customShutdownTimeout": None,
            "customRestoreTimeout": None,
            "geo_fence_type": "cart_control",
            "id_geofenceActionType": id_geofence_action_type,
            "points": coordinates,
            "defaultMessage": 1
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-access-token': 'bjVDR13m9pZq1wLRRlc2a-qNaqZDM2mbrv78Hnmx7oCZ1qO5hrhnk5AX9mTr'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def course_geofence_pro_tips_create(self, coordinates, pro_tip_hole_number, pro_tip_message="PRO_TIP"):
        """
        Create course geofence ProTips
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_geofenceType": 15,
            "id_company": self.id_company,
            "name": f'Hole {pro_tip_hole_number} - Pro Tip',
            "id_course": self.id_course,
            "proTipHoleNumber": pro_tip_hole_number,
            "proTipMessage": pro_tip_message + " HOLE " + str(pro_tip_hole_number),
            "points": coordinates
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-access-token': 'nkQiNRoRsVa0B-uxO79sw-1f82u0HVvIFFuPyKUD4IOPJscv-64lxFd2bufQ'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def course_geofence_cart_path_create(self,name, coordinates, id_coursecheckpoint): # superior id_coursecheckpoint 3173-3190
        """
        Create course geofence Cart Path
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_company": self.id_company,
            "id_geofenceType": 18,
            "points": coordinates,
            "name": name,
            "geo_fence_type": "cart_path",
            "id_coursecheckpoint": id_coursecheckpoint
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'x-access-token': 'NvOzltkl8f7AlxbxHARoV1cNOBAPYrd4CDi2xCpn6sHVLAnqj0UIFKplWJKy'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


    def convert_coordinates_to_float(self, coordinates):
        """Функция для преобразования строковых координат в тип float"""
        converted_coordinates = []
        for coord in coordinates:
            lat = float(coord["lat"])
            lng = float(coord["lng"])
            converted_coordinates.append({"lat": lat, "lng": lng})
        return converted_coordinates

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

    def course_geofence_advertisement_type_create(self, name, file_name='image.jpg', coordinates=None):
        """
        Create course geofence advertisement type
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = {
            'request': json.dumps({
                "fileType": "image/jpeg",
                "companyCode": self.company_code,
                "active": 1,
                "id_company": self.id_company,
                "geofenceStatus": 1,
                "visible": 1,
                "id_geofenceType": 17,
                "marshallBypass": 1,
                "disabilityBypass": 0,
                "name": name,
                "points": coordinates
            }),
        }

        files = [('file', (file_name, open(f'downloaded_images/{file_name}', 'rb'), 'image/jpeg'))]

        headers = {
            'authority': self.host,
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'origin': self.url,
            'referer': self.url,
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

    def course_geofence_advertisement_download_file(self, name, image_url):
        """Отправить GET-запрос для загрузки изображения"""
        response = requests.get(image_url)
        if response.status_code == 200:
            # Открыть файл для записи в бинарном режиме
            with open(f"downloaded_images/{name}.jpg", "wb") as file:
                # Записать полученные данные в файл
                file.write(response.content)
            print("Изображение успешно скачано")
        else:
            print("Ошибка при скачивании изображения. Код статуса:", response.status_code)

    def course_geofence_advertisement_type_turn_off(self, id_geofence):
        # url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceUpdate/FVyzsVqr-BmP280/QA/1.0/2.0/HmacSHA256/jfC2MNAcNijykJPGY9Bytb_ZZEgS_tt_9k2EXFy3zF0/230830155134+0300/JSON"

        action = "CourseGeofenceUpdate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"

        payload = json.dumps({
            "id_geofence": id_geofence,
            "status": 0
        })
        headers = {
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin':self.url,
            'referer': self.url,
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-access-token': 'mBH0N6fxP_Lnz8nCkNn8zH5w67VX7m8F_a_IHBotPJGrWAFiDf3B1YoObC_G'
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
            'authority': self.host,
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-access-token': 'ZV6AcGrwX6sXgb5UZPspXhYk9q2oayu200_V6IX9A_c5QrXK9wEd2y4HuG6t'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
