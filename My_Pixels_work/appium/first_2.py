from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='192.168.3.220'
    )

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

wait = WebDriverWait(driver, 10)  # Максимальное время ожидания в секундах

button_menu = driver.find_element(MobileBy.ID, 'com.l1inc.yamatrack3d:id/buttonMenu')
button_menu.click()
print("CLICK BUTTON MENU")

wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings')))
button_settings = driver.find_element(MobileBy.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings')
button_settings.click()
print("CLICK BUTTON SETTINGS")

wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.l1inc.yamatrack3d:id/textViewPasscode')))
text = driver.find_element(MobileBy.ID, 'com.l1inc.yamatrack3d:id/textViewPasscode')
print(text.text)

for i in '123999':
    button_id = f'com.l1inc.yamatrack3d:id/button{i}'
    driver.find_element(MobileBy.ID, button_id).click()
    print(f"PRESS BUTTON {i}")

wait.until(EC.element_to_be_clickable((MobileBy.ID, 'com.l1inc.yamatrack3d:id/buttonSubmit')))
driver.find_element(MobileBy.ID, 'com.l1inc.yamatrack3d:id/buttonSubmit').click()
print("PRESS SUBMIT")

wait.until(EC.element_to_be_clickable((MobileBy.ID, 'com.l1inc.yamatrack3d:id/listView')))
data = driver.find_element(MobileBy.ID, 'com.l1inc.yamatrack3d:id/listView')


