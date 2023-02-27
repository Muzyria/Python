#
# def point_in_polygon(point, polygon):
#     x, y = point
#     n = len(polygon)
#     inside = False
#
#     p1x, p1y = polygon[0]
#     for i in range(n + 1):
#         p2x, p2y = polygon[i % n]
#         if y > min(p1y, p2y):
#             if y <= max(p1y, p2y):
#                 if x <= max(p1x, p2x):
#                     if p1y != p2y:
#                         xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
#                     if p1x == p2x or x <= xints:
#                         inside = not inside
#         p1x, p1y = p2x, p2y
#
#     return inside
#
#
# """
# Здесь point - это проверяемая точка, заданная в виде кортежа координат (x, y),
#     а polygon - список вершин многоугольника,
#  каждая вершина задана в виде кортежа координат (x, y).
#   Функция point_in_polygon возвращает True,
#  если точка находится внутри многоугольника, и False в противном случае.
# """
import requests
import json

url = "https://dev-api.syncwise360.com/rest/action/CourseGeofenceList/FVyzsVqr-BmP280/igorperetssuperior/1.0/2.0/HmacSHA256/kxt8gN0sxeqsZj4yuP_iNNaS_RVnRV5aZ5gr6rl4UXY/230227153300+0200/JSON"

payload = json.dumps({
  "id_course": "xqrRgFzOAmmP",
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
  'x-access-token': 'Hks4KaNMc9IYyJTG2v7OQwjUwfRx3SrZFZrCg4v08mrKZb-lgXeN3hg8Osxe',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
