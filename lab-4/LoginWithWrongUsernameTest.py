from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import logging


class LoginWithWrongUsernameTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            logging.exception('Failed to set up the firefox web driver, error: %s', e)
        logging.basicConfig(level=logging.INFO)

    def test_login_with_wrong_username_failure_firefox(self):
        logging.info("Starting test_login_with_wrong_username_failure_firefox")
        self.login_failure(self.driver)

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception as e:
            logging.exception('Failed to set up the chrome web driver, error: %s', e)
        logging.basicConfig(level=logging.INFO)

    def test_login_with_wrong_username_failure_chrome(self):
        logging.info("Starting test_login_with_wrong_username_failure_with_chrome")
        self.login_failure(self.driver)

    def login_failure(self, driver):
        try:
            driver.get("https://practicetestautomation.com/practice-test-login")
            self.assertIn("Test Login | Practice Test Automation", driver.title)
            username = driver.find_element(By.ID, "username")
            password = driver.find_element(By.ID, "password")
            submit = driver.find_element(By.ID, "submit")

            username.send_keys("wrong_username")
            logging.info("Wrong username entered")
            password.send_keys("Password123")
            logging.info("Password entered")
            submit.click()
            logging.info("Submit button clicked")

            self.assertIn("https://practicetestautomation.com/practice-test-login", driver.current_url)
            logging.info("Login failure stay on thie same page verified")

            error_text_container = driver.find_element(By.ID, "error")
            self.assertTrue("Your username is invalid!" in error_text_container.text)
            logging.info("Error message verified")
        except Exception as e:
            logging.exception('An error occurred during the test, error: %s', e)

    def tearDown(self):
        try:
            self.driver.close()
            logging.info("Test completed")
        except Exception as e:
            logging.exception('Failed to tear down the test, error: %s', e)

if __name__ == "__main__":
    unittest.main()
