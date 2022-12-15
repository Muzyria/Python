# import asyncio
#
# async def main():
#     print('Hello ...')
#     await asyncio.sleep(10)
#     print('... World!')
#
# asyncio.run(main())


import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)

# action.click()
#  # Загрузить действие правого клика
# time.sleep(2)
#
# action.context_click()
#  # Выполнить все загруженные действия
# time.sleep(2)


# x=100
# y=100
# for i in range(100):
#     action.w3c_actions.pointer_action.move_to_location(i,i)
#     action.context_click()
#     action.perform()


actions = ActionChains(driver)
actions.move_by_offset(100, 100).perform()
time.sleep(5)
actions.context_click().perform()
time.sleep(5)
actions.click().perform()