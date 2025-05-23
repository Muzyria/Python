import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import By

os.system(f'adb disconnect')
os.system(f'adb connect 192.168.3.220')

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName=''
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
driver.implicitly_wait(10)

driver.long_press_keycode(26)
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.EditText').send_keys("102938")
driver.find_element(By.ID, 'android:id/button1').click()


element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]')

element.click()

driver.quit()
