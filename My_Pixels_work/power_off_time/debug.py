
from appium import webdriver

# desired_caps = {
#     'platformName': 'Android',
#     'udid': '192.168.3.219:5555',  # Замените на IP-адрес вашего устройства
#     'appPackage': 'com.android.settings',
#     'appActivity': '.Settings',
#     'noReset': 'true'
# }
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# # Пример: кликнуть на настройку "Date & Time"
# driver.find_element_by_android_uiautomator('text("Date & Time")').click()
#
# # Пример: получить текст параметра даты и времени
# date_time_text = driver.find_element_by_id('com.android.settings:id/date_time').text
# print(date_time_text)
#
# # Другие действия с элементами на экране настроек
# # ...
#
# driver.quit()

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'udid': '192.168.3.219',  # Замените на IP-адрес вашего устройства
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': 'true'
}

driver = webdriver.Remote('http://192.168.3.219:4723/wd/hub', desired_caps)

# Ваш код для взаимодействия с настройками

driver.quit()
