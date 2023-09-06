from run_power_off_time import Scheduler


test = Scheduler()

# test.open_date_settings()

test.check_devices_active("192.168.1.133")
print(test.get_value_new_time(5))
# test.put_time_off(test.set_power_of_time())

test.get_time_off()

test.get_random_power_off_time()



