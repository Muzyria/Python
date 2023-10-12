import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

capabilities = {
    "platformName": "android",
    "automationName": "uiautomator2",
    "deviceName": "dbe407da",
    "appPackage": "com.l1inc.yamatrack3d",
    # "language": "en",
    # "locale": "US"
}

appium_server_url = 'http://localhost:4723/wd/hub'

class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_click_menu(self):
        button = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.l1inc.yamatrack3d:id/buttonMenu"]')
        button.click()

if __name__ == '__main__':
    unittest.main()

