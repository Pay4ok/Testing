from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimpleSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def log(msg):
        print(msg)
