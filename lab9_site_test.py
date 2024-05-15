import unittest
from selenium import webdriver
from pages.lab9_site import SimpleSearchPage

class TestSimpleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = SimpleSearchPage(self.driver)

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

    def test_search(self):
        self.page.open()
        query = "'/.,;\"`-=)(*&&^"
        self.page.search_query(query)
        self.page.click_submit()
        self.page.check_error_message()

        input("Нажмите Enter для завершения теста...")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
