import os

start_coordinates = "50.07908030304553, 36.231179942837095"

for _ in range(10):
    print(start_coordinates)
    os.system(f'adb shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location "{start_coordinates}"')