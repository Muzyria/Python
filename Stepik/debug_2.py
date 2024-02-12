import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension(fr'C:\Users\FILA\Desktop\coordinates.crx')
# options_chrome.add_argument('--headless=new')

#with webdriver.Chrome(ChromeDriverManager().install()) as driver: # webdriver.Chrome(service=Service(ChromeDriverManager().install()))
with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome) as browser:
    # search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')))
    url = 'https://2ip.ua/'

    browser.get(url)
    browser.fullscreen_window()
    time.sleep(5)
    # print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    search = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="copy-clipboard"]')))
    print(search.get_attribute('data-clipboard-text'))
    time.sleep(5)




