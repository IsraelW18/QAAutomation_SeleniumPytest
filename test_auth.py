"""The file includes testing for users authentication - Signup. Login"""
import time
import string
import random
from selenium.webdriver.common.by import By
import pytest
import requests

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestSignUpUser:
    """
    Scenario_1.
    Test Description: SignUp a new user using valid credentials.
    """
    def test_signup_new_user(self, chrome_driver_setup, logger_setup):
        logger = logger_setup
        logger.debug("logger setup successfully")
        driver = chrome_driver_setup
        logger.debug("driver setup successfully")
        driver.get("https://carsphere.onrender.com/")
        logger.info("navigate to 'https://carsphere.onrender.com/' success")
        nav_links = driver.find_elements(By.XPATH, "//nav/a")
        for link in nav_links:
            if "register" in link.get_attribute("href"):
                link.click()
        logger.info("redirected to 'register page'")
        """TODO: changing the following to read input data from an external file,
        and populating the values using a loop"""

        # Generating a new random 'username' and checking that it do not already included in the DB
        response = requests.get("https://carsphere.onrender.com/get-users")
        existing_users = response.text
        random_username = "user3"
        while random_username in existing_users:
            random_username = "Auto_username" + ''.join(random.choices(string.digits, k=3))

        with open("users.txt", "a") as users_file:
            users_file.write(f"\n{random_username}")

        driver.find_element(By.ID, "firstname").send_keys("QAAuto_FirstName")
        driver.find_element(By.ID, "lastname").send_keys("QAAuto_LastName")
        driver.find_element(By.ID, "username").send_keys(random_username)
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "confirm_password").send_keys("1234")
        driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
        alert_success = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success").text
        assert "Welcome, QAAuto_FirstName QAAuto_LastName and thanks for registration!" in alert_success, "Failed to SignUp"
        print("Success QA")

    def test_signup_existing_user_in_db(self, chrome_driver_setup, logger_setup):
        pass