from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserManager:
    PAGE_URL = "https://elib.belstu.by/simple-search"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def open_with_params(self, params):
        url = f"{self.PAGE_URL}?{params}"
        self.driver.get(url)

    def search_query(self, query):
        search_input = self.driver.find_element(By.ID, "query")
        search_input.send_keys(query)

    def Connect(driver):
        driver.Connect();
