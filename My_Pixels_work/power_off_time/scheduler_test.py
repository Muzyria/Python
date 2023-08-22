from run_power_off_time import Scheduler


test = Scheduler()

test.check_devices_active("192.168.3.219")

test.get_time_off()
test.get_random_power_off_time()




