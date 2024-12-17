import time

from sincwise_clients_method import SyncwiseClient

payloads_live = {'superior': {
                    "host": "https://api2.syncwise360.com",
                    "url": "https://beta.syncwise360.com/",
                    "username": "igorperetssuperior",
                    "password": "Qwerty01!",
                    "id_company": "4442",
                    "id_course": "KoyhA-zWt6os",
                    "company_code": "HLxTfxrUaaI0"
                             },
                'disney': {
                    "host": "https://api2.syncwise360.com",
                    "url": "https://beta.syncwise360.com/",
                    "username": "igolfdisney",
                    "password": "92108340",
                    "id_company": "4820",
                    "id_course": "f1wKXtcAgZ1n",
                    "company_code": "whZVhCNHfCFM"
                          }
                }


payloads_dev = {'superior': {
                    "host": "https://dev-api.syncwise360.com",
                    "url": "https://sandbox.syncwise360.com",
                    "username": "igorperetssuperior",
                    "password": "Qwerty01!",
                    "id_company": "2973",
                    "id_course": "xqrRgFzOAmmP",
                    "company_code": "DDg2_tDaqpk7"
                            },
                }

"""INFO"""
"""Type Geofence
10 - Regular Geofence (when enter)
12 - # непонятный новый геофенс что то странное
13 - Regular Geofence (when leave) 

14 - Tournament Lock Down
15 - ProTips
16 - Cart Burn
17 - ADV
18 - Cart Path
"""

# # Новые координаты (центр) в формате словаря

# # Точка на старой карте в формате словаря
old_point = {"lat": 28.405254165089463, "lng": -81.58408369421585} # Disney
# Новые координаты (центр) в формате словаря
new_center = {"lat": 50.09005483768335, "lng": 36.23441078665438}   #  Superior


# Рассчитываем разницу в координатах
lat_diff = new_center["lat"] - old_point["lat"]
lng_diff = new_center["lng"] - old_point["lng"]


def convert_coordinates(center, coordinates, lat_diff, lng_diff):
    converted_coordinates = []
    for coord in coordinates:
        new_lat = center["lat"] + (coord["lat"] - old_point["lat"])
        new_lng = center["lng"] + (coord["lng"] - old_point["lng"])
        converted_coordinates.append({"lat": new_lat, "lng": new_lng})
    return converted_coordinates


disney_live = SyncwiseClient(**payloads_live['disney'])  # MAIN
disney_live.user_account_login()
disney_live.course_geofence_list()

superior_live = SyncwiseClient(**payloads_live['superior'])  # MAIN
superior_live.user_account_login()
superior_live.course_geofence_list()

# superior_dev = SyncwiseClient(**payloads_dev['superior'])  # MAIN
# superior_dev.user_account_login()
# superior_dev.course_geofence_list()


# s = [8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969, 8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969, 8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969]
# value_count = 0
# for item in disney_live.COURSE_GEOFENCE_LIST['resultList']:
#     if item['id_geofenceType'] == 17:
#         print(item)
#         print(id_geofence := item['id_geofence'])
#         # print(id_geofence_action_type := item['id_geofenceActionType'])
#
#         # LOAD IMAGE
#         data_url_image = disney_live.course_geofence_details(id_geofence)
#         print(name_geofence := item['name'])
#         disney_live.course_geofence_advertisement_download_file(id_geofence, data_url_image["adsImage"])
#
#
#         # print(points := item['points'])
#         print("---------------------------------------------------------------------------------")
#         # print(new_coord := superior_live.convert_coordinates_to_float(points))
#         # print(new_coord := convert_coordinates(new_center, superior_live.convert_coordinates_to_float(points), lat_diff, lng_diff))
#
#         time.sleep(1)
        # break


for item in disney_live.COURSE_GEOFENCE_LIST['resultList']:
    if item['id_geofenceType'] == 10:
        print(item)
        print(id_geofence := item['id_geofence'])
        print(id_geofence_action_type := item['id_geofenceActionType'])
        print(name_geofence := item['name'])
        print(points := item['points'])
        print(new_coord := convert_coordinates(new_center, superior_live.convert_coordinates_to_float(points), lat_diff, lng_diff))

#         # print(pro_tips_name := name_geofence.split(" ")[1])
#         # superior_live.course_geofence_pro_tips_create(new_coord, pro_tips_name, name_geofence)  # create pro tip type 15
#         time.sleep(2)


        superior_live.course_geofence_create(name_geofence, new_coord, id_geofence_action_type)  # regular create type 10

        # superior_live.course_geofence_advertisement_type_create(name_geofence, f'{id_geofence}.jpg', new_coord) # adv create type 17
        time.sleep(3)



