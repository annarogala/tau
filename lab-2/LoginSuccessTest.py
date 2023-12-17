from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import logging


class LoginSuccessTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            logging.exception('Failed to set up the firefox web driver, error: %s', e)
        logging.basicConfig(level=logging.INFO)

    def test_login_success_firefox(self):
        logging.info("Starting test_login_success_firefox")
        self.login_success(self.driver)

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception as e:
            logging.exception('Failed to set up the chrome web driver, error: %s', e)
        logging.basicConfig(level=logging.INFO)

    def test_login_success_chrome(self):
        logging.info("Starting test_login_success_chrome")
        self.login_success(self.driver)

    def login_success(self, driver):
        try:
            driver.get("https://practicetestautomation.com/practice-test-login")
            self.assertIn("Test Login | Practice Test Automation", driver.title)
            username = driver.find_element(By.ID, "username")
            password = driver.find_element(By.ID, "password")
            submit = driver.find_element(By.ID, "submit")

            username.send_keys("student")
            logging.info("Username entered")
            password.send_keys("Password123")
            logging.info("Password entered")
            submit.click()
            logging.info("Submit button clicked")

            self.assertIn("https://practicetestautomation.com/logged-in-successfully/", driver.current_url)
            logging.info("Login redirection verified")

            bodyText = driver.find_element(By.CLASS_NAME, "page").text
            self.assertTrue("Congratulations" in bodyText or "successfully logged in" in bodyText)
            logging.info("Login success message verified")

            logout = driver.find_element(By.LINK_TEXT, 'Log out')
            self.assertTrue(logout.is_displayed())
            logging.info("Logout button found")
        except Exception as e:
            logging.exception('An error occurred during the test, error: %s', e)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
