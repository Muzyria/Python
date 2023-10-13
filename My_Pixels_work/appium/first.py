import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import By

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    # deviceName='dbe407da',
    deviceName='192.168.3.220',
    # uiautomator2ServerInstallTimeout=30000,  # Увеличьте таймаут
    # appPackage='com.l1inc.yamatrack3d',
    # language='en',
    # locale='US'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/buttonMenu').click()
print("CLICK BUTTON MENU")
time.sleep(0.1)

driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings').click()
print("CLICK BUTTON SETTINGS")
time.sleep(0.1)

tex = driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/textViewPasscode')
print(tex.text)
# time.sleep()


for i in '123999':
    driver.find_element(By.ID, f'com.l1inc.yamatrack3d:id/button{i}').click()
    print(f"PRESS BUTTON {i}")
    # time.sleep()

driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/buttonSubmit').click()
print("PRESS SUBMIT")
time.sleep()



