import os
import time


def send_adb_command(ip_device, location):
    os.system(
        rf'adb -s {ip_device} shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

while True:
    ip = "dbe407da"
    location = "50.08150892692462, 36.23714019789124"
    send_adb_command(ip, location)
    # time.sleep(1)

