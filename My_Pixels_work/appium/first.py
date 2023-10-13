import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import By

capabilities = dict(
    platformName='android',
    # automationName='uiautomator2',
    deviceName='dbe407da',
    # appPackage='com.l1inc.yamatrack3d',
    # language='en',
    # locale='US'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/buttonMenu').click()
driver.find_element(By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings').click()


# appium_server_url = 'http://localhost:4723'
#
# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, capabilities)
#
#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()
#
#
#     def test_click_menu(self) -> None:
#          buton = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.l1inc.yamatrack3d:id/buttonMenu"]')
#          buton.click()
#
#
#
# if __name__ == '__main__':
#     unittest.main()
