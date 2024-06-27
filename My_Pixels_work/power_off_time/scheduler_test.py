from run_power_off_time import Scheduler


test = Scheduler("192.168.0.101")

# test.open_date_settings()
test.check_devices_active()
# print(test.get_value_new_time(5))
# new_time = test.get_value_new_time(minutes=1, minutes_pw_off=1)
#
# test.put_time_off(new_time[0])
# test.put_random_power_off_time(new_time[1])
#
# test.get_time_off()
# test.get_random_power_off_time()
# test.open_date_settings()

# print(test.__dict__)
