# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit")

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service(r'/home/fila/Загрузки/chromedriver')
# service.start()
# driver = webdriver.Remote(service.service_url)
# driver.get('http://www.google.com/')
# time.sleep(5) # Let the user actually see something!
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# s = Service(r'/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(service=s)
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]')  # data-test XPATH
# user_name.send_keys("standard_user")
# password = driver.find_element(By.CSS_SELECTOR, '#password')  # CSS
# password.send_keys("secret_sauce")
# button_login = driver.find_element(By.XPATH, "//input[@value='Login']")  # XPATH
# button_login.click()
# time.sleep(3)
# driver.close()

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.python.org")
# driver.close()
