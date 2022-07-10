from selenium.webdriver.common.by import By
from random import randint


class FormPageLocators:
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1, 3)}"]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')

