from appium import webdriver

desired_caps = {
  "platformName": "Android",
  "deviceName": "YOUR_DEVICE_NAME",
  "appPackage": "YOUR_APP_PACKAGE",
  "appActivity": "YOUR_APP_ACTIVITY"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
