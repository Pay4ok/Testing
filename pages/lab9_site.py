from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimpleSearchPage:
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

    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "main-query-submit")
        submit_button.click()

    def check_error_message(self):
        error_message_locator = (By.CSS_SELECTOR, "p.submitFormWarn")
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(error_message_locator)
            )
            error_text = error_element.text
            assert "An error has occurred. Your query is invalid or the search engine is down." in error_text, \
                "Expected error message not found"
        except Exception as e:
            raise AssertionError("Expected error message not found on the page.") from e
