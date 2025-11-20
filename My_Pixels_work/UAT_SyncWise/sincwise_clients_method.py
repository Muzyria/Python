import time
import requests
import json
from create_signature_class import SyncwiseAPI
import math


def calculate_circle_points(center_shape, diameter, num_points=16) -> list[dict]:
    latitude, longitude = center_shape
    radius = diameter / 2  # радиус в метрах
    earth_radius = 6371000  # радиус Земли в метрах

    points_list = []
    for angle in range(0, 360, int(360 / num_points)):
        angle_rad = math.radians(angle)

        # Смещение в градусах
        delta_lat = (radius / earth_radius) * (180 / math.pi)
        delta_lon = (radius / earth_radius) * (180 / math.pi) / math.cos(math.radians(latitude))

        # Вычисление координат новой точки
        new_lat = latitude + delta_lat * math.sin(angle_rad)
        new_lon = longitude + delta_lon * math.cos(angle_rad)

        points_list.append({'lat': new_lat, 'lng': new_lon})
        # points_list.append(points[0])
    return points_list

# # Пример использования
# center = (36.2451303225386, 50.08329004978064)
# diameter = 50  # в метрах
# points = calculate_circle_points(center, diameter)
#
# for i, point in enumerate(points):
#     print(f"Point {i + 1}: {point}")


class SyncwiseClient:
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



    # PRIVATE
    def course_vector_details(self):
        """
        Get course vector details
        """

        # читаем и парсим JSON
        with open("VectorData.json", "r") as f:
            data = json.load(f)

        # если хочешь сохранить весь словарь в атрибут
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


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test_1 = SyncwiseClient()

    test_1.course_vector_details()

    print(test_1.COURSE_VECTOR_DETAILS)

