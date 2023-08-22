from run_power_off_time import Scheduler


test = Scheduler()

test.check_devices_active("192.168.3.219")


test.put_random_power_off_time(1412)
test.get_random_power_off_time()


