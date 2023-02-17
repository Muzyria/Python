import requests


class Test_new:


    def ntest_new(self):


        base_url = "https://api-dna.igolf.com/rest/action/"  # базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов

        """Создание новой локации"""
        post_resource = "UserAccountLogin/uUqnXUKU86kghJk/1.0/2.0/HmacSHA256/2Wx7AIBZ4ctGrThUZVTWgvyq-qVGYz2NVDW9SbHQgyQ/221229151003GMT+02:00/JSON"  # Ресурс метода пост

        post_url = base_url + post_resource
        print(post_url)

        json_new = {
                            "username": "igolfsaltcreek",
                            "password": "92108340"
                            }

        result_post = requests.post(post_url, json=json_new)
        print(result_post.text)


        assert 200 == result_post.status_code
        print("Успешно!!! ")
        print(type(esult_post.json())

        check_post = result_post.json()
        check_info_post = check_post.get("status")

        # print(f'Статус код ответа : {check_info_post}')
        # assert check_info_post == "OK"
        # print("Статус код ответа верен")
        # place_id = check_post.get("place_id")
        # print(f'place_id ответа : {place_id}')








new_place = Test_new()
new_place.ntest_new()
