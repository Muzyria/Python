# import pytest
# from appium import webdriver
# from appium.webdriver.common.mobileby import AppiumBy
#
# capabilities = {
#     'platformName': 'android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'dbe407da'
# }
#
# appium_server_url = 'http://127.0.0.1:4723/'
#
# @pytest.fixture(scope="function")
# def appium_driver():
#     driver = webdriver.Remote(appium_server_url, capabilities)
#     yield driver
#     driver.quit()
#
# def test_find_battery(appium_driver):
#     el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
#     el.click()


import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='dbe407da',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    # language='en',
    # locale='US'
)

appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope="function")
def appium_driver():
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()


def test_find_battery(appium_driver):
    el = appium_driver.find_element(by=AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
    el.click()