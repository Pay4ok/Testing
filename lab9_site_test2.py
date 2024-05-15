import unittest
from selenium import webdriver
from pages.lab9_site import SimpleSearchPage

class TestInvalidSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = SimpleSearchPage(self.driver)

    def test_invalid_query(self):
        params = "location=%2F&query=&rpp=[]"
        self.page.open_with_params(params)
        self.page.check_error_message()

        # Добавим паузу для того, чтобы браузер остался открытым
        input("Нажмите Enter для завершения теста...")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
