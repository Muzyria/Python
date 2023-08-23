from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'udid': '192.168.3.127',  # Замените на IP-адрес вашего устройства
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': 'true'
}

driver = webdriver.Remote('http://192.168.3.127:4723/wd/hub', desired_caps)

# Ваш код для взаимодействия с настройками

driver.quit()
