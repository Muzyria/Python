import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

capabilities = dict(
    platformName='android',
    automationName='uiautomator2',
    deviceName='dbe407da',
    appPackage='com.l1inc.yamatrack3d',
    # appActivity='.activities.MapActivity10Inch_',
    # language='en',
    # locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    # def test_find_battery(self) -> None:
    #     el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    #     el.click()

    def test_click_menu(self) -> None:
         buton = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@id="com.l1inc.yamatrack3d:id/buttonMenu"]')
         buton.click()




if __name__ == '__main__':
    unittest.main()
