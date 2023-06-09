import requests
import json
import create_signature
from create_signature_class import SyncwiseAPI


# api = SyncwiseAPI("https://dev-api.syncwise360.com")


class SyncwiseClient(SyncwiseAPI):
    SECRET_KEY = None
    COURSE_GEOFENCE_LIST = None
    COURSE_VECTOR_DETAILS = None

    # PUBLIC
    def user_account_login(self):
        """
        Login user and get secret key
        """
        url = f"{self.host}/rest/action/{self.create_url_test_with_public()}"

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
        self.SECRET_KEY = response_data['secretKey']

    # PRIVATE
    def course_geofence_list(self):
        """
        Get course geofence list
        """
        action = "CourseGeofenceList"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_company": 2973,
            "active": 1
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'https://sandbox.syncwise360.com/',
            'x-access-token': '72Y8ItBOOQT2S2u41cosMWw_hSjrpOreSND8N9iRaoO1B3k3wmUPA7dxt3yb',
            'sec-ch-ua-platform': '"Windows"'
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

    def course_vector_details(self):
        """
        Get course vector details
        """
        action = "CourseVectorDetails"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "id_course": "xqrRgFzOAmmP"
        })
        headers = {
            'authority': 'dev-api.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://sandbox.syncwise360.com',
            'referer': 'https://sandbox.syncwise360.com/',
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

    def course_geofence_create(self):
        """
        Create course geofence
        """
        action = "CourseGeofenceCreate"
        url = f"{self.host}/rest/action/{self.create_url_test_with_private(action, self.SECRET_KEY)}"
        payload = json.dumps({
            "active": 1,
            "status": 1,
            "visible": 1,
            "id_company": 2973,
            "id_geofenceType": 10,
            "name": "222",
            "marshallBypass": 1,
            "disabilityBypass": 1,
            "controlLevel": 22,
            "customShutdownTimeout": None,
            "customRestoreTimeout": None,
            "geo_fence_type": "cart_control",
            "id_geofenceActionType": 60,
            "points": [{"lat": 50.089809146357, "lng": 36.23908154605},
                       {"lat": 50.088254317432, "lng": 36.234594210368},
                       {"lat": 50.088240550044, "lng": 36.234556659442},
                       {"lat": 50.088225061728, "lng": 36.234529837352},
                       {"lat": 50.088200968782, "lng": 36.234500333053},
                       {"lat": 50.088178596749, "lng": 36.234476193172},
                       {"lat": 50.087686409398, "lng": 36.234114094955},
                       {"lat": 50.08766575807, "lng": 36.234100683909},
                       {"lat": 50.087650269568, "lng": 36.234095319491},
                       {"lat": 50.087621013495, "lng": 36.234087272864},
                       {"lat": 50.087591757405, "lng": 36.234084590655},
                       {"lat": 50.087560780348, "lng": 36.234084590655},
                       {"lat": 50.087526361373, "lng": 36.234087272864},
                       {"lat": 50.086249830172, "lng": 36.234209313375},
                       {"lat": 50.086235201711, "lng": 36.234211995584},
                       {"lat": 50.086217131252, "lng": 36.234218701106},
                       {"lat": 50.086204223777, "lng": 36.234228088838},
                       {"lat": 50.086192176798, "lng": 36.234240158778},
                       {"lat": 50.086182711312, "lng": 36.234252228719},
                       {"lat": 50.086169803828, "lng": 36.234273686391},
                       {"lat": 50.086154314843, "lng": 36.23430319069},
                       {"lat": 50.086145709849, "lng": 36.234327330571},
                       {"lat": 50.086137104853, "lng": 36.23435683487},
                       {"lat": 50.086132802355, "lng": 36.234375610333},
                       {"lat": 50.086130220856, "lng": 36.23439840911},
                       {"lat": 50.086130220856, "lng": 36.234423890096},
                       {"lat": 50.086132802355, "lng": 36.23445205329},
                       {"lat": 50.086141407351, "lng": 36.234486922008},
                       {"lat": 50.086150012346, "lng": 36.234511061889},
                       {"lat": 50.086169803828, "lng": 36.234559341651},
                       {"lat": 50.08618443231, "lng": 36.234591528159},
                       {"lat": 50.086199921285, "lng": 36.234625055772},
                       {"lat": 50.086212828761, "lng": 36.234645172339},
                       {"lat": 50.086231759719, "lng": 36.23467199443},
                       {"lat": 50.08655745708, "lng": 36.234985812884},
                       {"lat": 50.086584992818, "lng": 36.235004588347},
                       {"lat": 50.086626296397, "lng": 36.235023363811},
                       {"lat": 50.0874592443, "lng": 36.23538009761},
                       {"lat": 50.087479895717, "lng": 36.235388144237},
                       {"lat": 50.087502268076, "lng": 36.235404237491},
                       {"lat": 50.08753324517, "lng": 36.235431059581},
                       {"lat": 50.08754873371, "lng": 36.235457881671},
                       {"lat": 50.08816482934, "lng": 36.236723884326},
                       {"lat": 50.088178596749, "lng": 36.236753388625},
                       {"lat": 50.08819408508, "lng": 36.236780210715},
                       {"lat": 50.088206131557, "lng": 36.236800327283},
                       {"lat": 50.089665023495, "lng": 36.239202245456},
                       {"lat": 50.089671906984, "lng": 36.239212974292},
                       {"lat": 50.089681371781, "lng": 36.239219679814},
                       {"lat": 50.089693417884, "lng": 36.239221020919},
                       {"lat": 50.089714068338, "lng": 36.239221020919},
                       {"lat": 50.089735579219, "lng": 36.239215656501},
                       {"lat": 50.08975536922, "lng": 36.239208950978},
                       {"lat": 50.089771717476, "lng": 36.239200904351},
                       {"lat": 50.089783763556, "lng": 36.239194198829},
                       {"lat": 50.089792367897, "lng": 36.239186152202},
                       {"lat": 50.089800972236, "lng": 36.23917676447},
                       {"lat": 50.089806134839, "lng": 36.239168717843},
                       {"lat": 50.089810437007, "lng": 36.239156647903},
                       {"lat": 50.089813018308, "lng": 36.239143236857},
                       {"lat": 50.089814739176, "lng": 36.239128484708},
                       {"lat": 50.089813878742, "lng": 36.239109709245},
                       {"lat": 50.089811297441, "lng": 36.2390962982},
                       {"lat": 50.089809146357, "lng": 36.23908154605}]

            ,
            # "points": [
            #     {
            #         "lat": 50.0892544142621,
            #         "lng": 36.23102188110352
            #     },
            #     {
            #         "lat": 50.091457100110425,
            #         "lng": 36.23235225677491
            #     },
            #     {
            #         "lat": 50.08972249347597,
            #         "lng": 36.23415470123292
            #     }
            # ],
            "defaultMessage": 1
        })
        headers = {
            'authority': 'dev-api.syncwise360.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://sandbox.syncwise360.com',
            'referer': 'https://sandbox.syncwise360.com/',
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


test_1 = SyncwiseClient("https://dev-api.syncwise360.com")
test_1.user_account_login()
# print(test_1.SECRET_KEY)
# test_1.course_geofence_list()
test_1.course_vector_details()
# print(test_1.COURSE_VECTOR_DETAILS)
test_1.course_geofence_create()
