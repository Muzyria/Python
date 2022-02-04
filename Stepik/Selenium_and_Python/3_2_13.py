# -*- coding: utf-8 -*- 
from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_class_name("first").send_keys("j")
        browser.find_element_by_class_name("second").send_keys("j")
        browser.find_element_by_class_name("third").send_keys("j")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual("Registration" != welcome_text, True, "Should be absolute value of a number")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_class_name("first").send_keys("j")
        browser.find_element_by_xpath("second").send_keys("j")
        browser.find_element_by_class_name("third").send_keys("j")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual("Registration" != welcome_text, True, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main() 