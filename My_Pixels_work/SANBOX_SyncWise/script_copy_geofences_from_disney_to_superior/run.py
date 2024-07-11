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
                    "username": "SyncwiseDisney",
                    "password": "92108340",
                    "id_company": "4820",
                    "id_course": "f1wKXtcAgZ1n",
                    "company_code": ""
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
# new_center = {"lat": 50.0856375, "lng": 36.2198086}
# # Точка на старой карте в формате словаря
old_point = {"lat": 28.4037203, "lng": -81.5869747} # Disney
# Новые координаты (центр) в формате словаря
new_center = {"lat": 50.09844995667801, "lng": 36.257673034667976}   # 36.247673034667976
# Точка на старой карте в формате словаря
# old_point = {"lat": 50.0856375, "lng": 36.2198086}
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


# disney_live = SyncwiseClient(**payloads_live['disney'])  # MAIN
# disney_live.user_account_login()
# disney_live.course_geofence_list()

# superior_live = SyncwiseClient(**payloads_live['superior'])  # MAIN
# superior_live.user_account_login()
# superior_live.course_geofence_list()

superior_dev = SyncwiseClient(**payloads_dev['superior'])  # MAIN
superior_dev.user_account_login()
superior_dev.course_geofence_list()


# s = [8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969, 8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969, 8952, 8953, 8954, 8955, 8956, 8957, 8958, 8959, 8960, 8961, 8962, 8963, 8964, 8965, 8966, 8967, 8968, 8969]
value_count = 0
for item in superior_dev.COURSE_GEOFENCE_LIST['resultList']:
    if item['id_geofenceType'] == 10 and "Evergreens" in item['name']:
        print(item)
        print(id_geofence := item['id_geofence'])
        # print(id_geofence_action_type := item['id_geofenceActionType'])
        print(name_geofence := item['name'])
        # print(points := item['points'])
        # print(new_coord := superior_dev.convert_coordinates_to_float(points))
        # print(new_coord := convert_coordinates(new_center, superior_dev.convert_coordinates_to_float(points), lat_diff, lng_diff))

        superior_dev.course_geofence_advertisement_type_delete(id_geofence)
        # break





# for item in disney_live.COURSE_GEOFENCE_LIST['resultList']:
#     if item['id_geofenceType'] == 10:
#         print(item)
#         print(id_geofence := item['id_geofence'])
#         print(id_geofence_action_type := item['id_geofenceActionType'])
#         print(name_geofence := item['name'])
#         print(points := item['points'])
#         print(new_coord := convert_coordinates(new_center, superior_dev.convert_coordinates_to_float(points), lat_diff, lng_diff))
#
#         superior_dev.course_geofence_create(name_geofence + '_10', new_coord, id_geofence_action_type)

