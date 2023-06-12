import os
from datetime import datetime

start_coordinates = "50.07807852323376, 36.23065154766116"



for _ in range(50):  # start coordinate for begin
    time_minute = datetime.now().time().minute
    os.system(rf'adb shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{start_coordinates}\"')
    if (now := datetime.now().time().minute) != time_minute:
        print(now, time_minute)
        time_minute = now
        os.system(rf'adb shell input tap 700 500')
        print(f'TOUCH SCREEN in {datetime.now().time()}')