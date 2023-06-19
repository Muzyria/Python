import multiprocessing



def send_adb_command(ip_device, start_coordinates):
    os.system(rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{start_coordinates}\"')

def get_start_coordinates():
    start_coordinates = "50.07807852323376, 36.23065154766116"
    pool = multiprocessing.Pool()
    for _ in range(5):  # start coordinate for begin
        time_minute = datetime.now().time().minute
        for ip_device in self.DICT_IP_DEVICES.values():
            pool.apply_async(send_adb_command, args=(ip_device, start_coordinates))
        pool.close()
        pool.join()
        if (now := datetime.now().time().minute) != time_minute:
            time_minute = now
            self.touch_screen()




def send_adb_command(ip_device, location):
    os.system(rf'adb -s {ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')

def run_device(steps):
    for i in range(1, self.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT + 1):
        for step_patch in self.get_intermediate_coordinates(self.client_data.COURSE_VECTOR_DETAILS_HOLES_CENTRALPATH[i], steps):
            lat, lng = step_patch['lat'], step_patch['lng']
            print(f'step -> {lat}, {lng}')
            pool = multiprocessing.Pool()
            time_minute = datetime.now().time().minute
            for ip_device in self.DICT_IP_DEVICES.values():
                pool.apply_async(send_adb_command, args=(ip_device, f"{lat}, {lng}"))
            pool.close()
            pool.join()
            if (now := datetime.now().time().minute) != time_minute:
                time_minute = now
                self.touch_screen()
