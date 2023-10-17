import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

capabilities = {
    'platformName': 'android',
    'automationName': 'uiautomator2',
    'deviceName': '192.168.3.221'
}

appium_server_url = 'http://127.0.0.1:4723/wd/hub'

@pytest.fixture(scope="function")
def appium_driver():
    driver = webdriver.Remote(appium_server_url, capabilities)
    yield driver
    driver.quit()

def test_find_battery(appium_driver):
    el = appium_driver.find_element(by=MobileBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
    el.click()
