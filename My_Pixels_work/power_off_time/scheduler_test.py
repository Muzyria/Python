from run_power_off_time import Scheduler


test = Scheduler()

test.check_devices_active("192.168.1.133")
print(test.set_power_of_time())
# test.put_time_off(test.set_power_of_time())

test.get_time_off()

test.get_random_power_off_time()



