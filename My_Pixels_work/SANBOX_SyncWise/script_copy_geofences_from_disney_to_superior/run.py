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

test_1 = SyncwiseClient(**payloads_live['superior'])  # MAIN
test_1.user_account_login()

print('SECRET KEY ->', end=' ')
print(test_1.SECRET_KEY)

coord = [{'lat': 50.0940599, 'lng': 36.2164416}, {'lat': 50.091650099999995, 'lng': 36.2165305}, {'lat': 50.0912612, 'lng': 36.216888899999994}, {'lat': 50.0909237, 'lng': 36.217313499999996}, {'lat': 50.0907136, 'lng': 36.2175485}, {'lat': 50.0903953, 'lng': 36.2176567}, {'lat': 50.08968779999999, 'lng': 36.2177318}, {'lat': 50.089697199999996, 'lng': 36.2177532}, {'lat': 50.087364699999995, 'lng': 36.2194704}, {'lat': 50.085031199999996, 'lng': 36.220951899999996}, {'lat': 50.0847929, 'lng': 36.221039299999994}, {'lat': 50.0816468, 'lng': 36.2222482}, {'lat': 50.0795238, 'lng': 36.224318399999994}, {'lat': 50.07759899999999, 'lng': 36.226538600000005}, {'lat': 50.076473299999996, 'lng': 36.225468799999994}, {'lat': 50.076303499999995, 'lng': 36.222090099999996}, {'lat': 50.0754428, 'lng': 36.2208769}, {'lat': 50.0741972, 'lng': 36.2202763}, {'lat': 50.071404199999996, 'lng': 36.218763900000006}, {'lat': 50.069682799999995, 'lng': 36.2160881}, {'lat': 50.0700508, 'lng': 36.2116368}, {'lat': 50.0804638, 'lng': 36.2115442}, {'lat': 50.0793882, 'lng': 36.2052802}, {'lat': 50.080298799999994, 'lng': 36.2021765}, {'lat': 50.0822613, 'lng': 36.199356400000006}, {'lat': 50.0829392, 'lng': 36.1985932}, {'lat': 50.083823499999994, 'lng': 36.1987102}, {'lat': 50.08571, 'lng': 36.200408700000004}, {'lat': 50.0892157, 'lng': 36.2004753}, {'lat': 50.0902063, 'lng': 36.2062352}, {'lat': 50.0912158, 'lng': 36.208337500000006}, {'lat': 50.0909843, 'lng': 36.210108600000005}, {'lat': 50.0929655, 'lng': 36.2124684}, {'lat': 50.0938618, 'lng': 36.2136482}, {'lat': 50.094220299999996, 'lng': 36.21413929999999}, {'lat': 50.09419199999999, 'lng': 36.214688599999995}, {'lat': 50.0940599, 'lng': 36.2164416}]


test_1.course_geofence_pro_tips_create(coord, 1)
# test_1.course_geofence_list()
# # print(test_1.COURSE_GEOFENCE_LIST)
#
# value_count = {}
# for item in test_1.COURSE_GEOFENCE_LIST['resultList']:
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
#     if item['id_geofenceType'] == 17:
#         print(id_geofence := item['id_geofence'])
#         data_url_image = test_1.course_geofence_details(id_geofence)
#         print(data_url_image["adsImage"])
#         test_1.course_geofence_advertisement_download_file(id_geofence, data_url_image["adsImage"])



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




# for number in range(1, 331):
#     # Генерировать случайный центр в заданных границах квадрата
#     random_target_square = test_1.generate_random_target_square(min_square_lat, max_square_lat, min_square_lng, max_square_lng)
#     # Переместить геофенс в случайный квадрат
#     moved_geofence = test_1.move_geofence_to_square(geofence, random_target_square)
#     # test_1.course_geofence_advertisement_type_create(f"adv_type_{number}", moved_geofence)
#     test_1.course_geofence_create(f"regular_type_{number}", moved_geofence)
#     print(f"GEOFENCE --- {number} CREATED")


