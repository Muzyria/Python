from appium import webdriver
from applitools.selenium import Eyes

class HelloWorld:

    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()
    eyes.api_key = 'YOUR_API_KEY'

    # Desired capabilities.
    desired_caps = dict(
        platformName = 'Android',
        deviceName = 'DEVICE_NAME',
        platformVersion= 'PLATFORM_VERSION',
        automationName= 'UiAutomator2',
        app='https://applitools.jfrog.io/artifactory/Examples/eyes-hello-world.apk')

    # Open the app.
    wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    wd.implicitly_wait(60)

    try:

        # Start the test.
        eyes.open(driver=wd, app_name='Contacts', test_name='My first Appium native Python test!')

        # Visual UI testing.
        eyes.check_window('Contact list!')

        # End the test.
        eyes.close()

    finally:

        # Close the app.
        wd.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort_if_not_closed()
