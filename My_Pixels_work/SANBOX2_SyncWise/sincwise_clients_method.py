import time

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
        url = f"{self.host}/auth-service/action/{self.create_url_test_with_public()}"

        payload = json.dumps({
            # "username": "nessahills2",  # Par 3-Pine Hills
            # "password": "Nesss!123"

            "username": "eighteendev",  # Eighteen-Sleepy Hollow Country Club
            "password": "Qwerty01!"

            # "username": "olehangels",  # Angels View-Oakville Executive Golf Courses 9 holes
            # "password": "Qwerty01!"
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'https://sandbox2.syncwise360.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response_data = response.json()
        print(response.text)
        self.SECRET_KEY = response_data['secretKey']

    # PRIVATE
    def course_vector_details(self, id_course):
        """
        Get course vector details
        """
        action = "CourseVectorDetails"
        url = f"{self.host}/main-service/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            # "id_course": "xqrRgFzOAmmP"
            "id_course": id_course
        })
        headers = {
            'authority': 'dev-api-gateway.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://sandbox2.syncwise360.com',
            'referer': 'https://sandbox2.syncwise360.com/',
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
        # print(data)
        self.COURSE_VECTOR_DETAILS = data


        self.COURSE_VECTOR_DETAILS_HOLECOUNT = data['vectorGPSObject']['HoleCount']


        self.COURSE_VECTOR_DETAILS_HOLES = data['vectorGPSObject']['Holes']['Hole']

        # Write data for hole shape clubhouse
        point_str = data['vectorGPSObject']['Clubhouse']['Shapes']['Shape'][0]['Points']
        self.COURSE_VECTOR_DETAILS_CLUBHOUSE[1] = [
            {"lat": float(i.split()[1]), "lng": float(i.split()[0])} for i in point_str.split(",")]

        # Write data for hole shape background
        point_str = data['vectorGPSObject']['Background']['Shapes']['Shape'][0]['Points']
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



if __name__ == '__main__':

    test_1 = SyncwiseClient("https://dev-api-gateway.syncwise360.com")
    test_1.user_account_login()

    print(test_1.SECRET_KEY)

    test_1.course_vector_details("GsVhpjLhrEIy")

    print(test_1.COURSE_VECTOR_DETAILS)
