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

# Новые координаты (центр) в формате словаря
new_center = {"lat": 50.0856375, "lng": 36.2198086}
# Точка на старой карте в формате словаря
old_point = {"lat": 28.4037203, "lng": -81.5869747}
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

superior_dev = SyncwiseClient(**payloads_dev['superior'])  # MAIN
superior_dev.user_account_login()

print('SECRET KEY ->', end=' ')
print(disney_live.SECRET_KEY)

print('SECRET KEY ->', end=' ')
print(superior_dev.SECRET_KEY)

# disney_live.course_geofence_list()
# superior_dev.course_geofence_list()


# print('disney -----')

# print(disney_live.COURSE_GEOFENCE_LIST)
#
# print('superior -----')
# print(superior_dev.COURSE_GEOFENCE_LIST)



# value_count = {}

# for item in disney_live.COURSE_GEOFENCE_LIST['resultList']:
#     if item['id_geofenceType'] == 18:
#         print(item)
    #     print(id_geofence := item['id_geofence'])
    #     # print(id_geofence_action_type := item['id_geofenceActionType'])
    #     print(name_geofence := item['name'])
    #     print(points := item['points'])
    #     print(new_coord := convert_coordinates(new_center, disney_live.convert_coordinates_to_float(points), lat_diff, lng_diff))
    #
    #     superior_dev.course_geofence_pro_tips_create(new_coord, )



#
#     print(item['id_geofenceType'], end=" -> ")
#     print(item)
#     value = item['id_geofenceType']
#     if value in value_count:
#         value_count[value] += 1
#     else:
#         value_count[value] = 1
#
# print(value_count)
# print(sum([int(i) for i in value_count.values()]))




# print(test_1.COURSE_GEOFENCE_LIST["resultList"])


# for item in test_1.COURSE_GEOFENCE_LIST["resultList"]:
#     if item["id_geofenceType"] == 10 and "regular_type" in item["name"]:
#         print(f'{item["name"]} {item["id_geofence"]}')


# adv_list = [item["id_geofence"] for item in test_1.COURSE_GEOFENCE_LIST["resultList"] if item["id_geofenceType"] == 10 and "regular_type" in item["name"]]
    # if item["id_geofenceType"] == 17:
    #     print(f'{item["name"]} {item["id_geofence"]}')
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


# min_square_lat = 50.08022234377751
# max_square_lat = 50.09313658004037
#
# min_square_lng = 36.24363899230958
# max_square_lng = 36.25930309295655
#
#
# geofence = [
#   {
#     "lat": 50.090761888323954,
#     "lng": 36.24425053596497
#   },
#   {
#     "lat": 50.091006246091446,
#     "lng": 36.24435245990754
#   },
#   {
#     "lat": 50.090834163286345,
#     "lng": 36.24464213848115
#   }
# ]




# for number in range(1, 331):
#     # Генерировать случайный центр в заданных границах квадрата
#     random_target_square = test_1.generate_random_target_square(min_square_lat, max_square_lat, min_square_lng, max_square_lng)
#     # Переместить геофенс в случайный квадрат
#     moved_geofence = test_1.move_geofence_to_square(geofence, random_target_square)
#     # test_1.course_geofence_advertisement_type_create(f"adv_type_{number}", moved_geofence)
#     test_1.course_geofence_create(f"regular_type_{number}", moved_geofence)
#     print(f"GEOFENCE --- {number} CREATED")


