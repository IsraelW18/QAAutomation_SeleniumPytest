"""This module includes testing for users authentication - Signup. Login"""
import string
import random
from selenium.webdriver.common.by import By
import pytest
import requests
import json

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestSignUpUser:
    """This class groups the 'Sign-up' testing actions"""

    """Scenario_1."""
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.functional
    def test_001_signup_new_user(self, chrome_driver_setup, logger_setup):
        """
        Test Description: SignUp a new user using valid credentials.
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_1 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        # Redirection to 'SignUp' page
        nav_links = driver.find_elements(By.XPATH, "//nav/a")
        for link in nav_links:
            if "register" in link.get_attribute("href"):
                link.click()
        logger.info("redirect to 'register page'")
        """TODO: changing the following to read input data from an external file,
        and populating the values using a loop"""

        # Generating a new random 'username' and checking that it do not already included in the DB
        # First: getting a list of all existing usernames from DB
        response = requests.get("https://carsphere.onrender.com/get-users")
        existing_users = response.text
        logger.debug(f"getting all existing users from DB:\n{existing_users}")
        # Second: Generating a new random username and checking that it is not exist already in DB
        random_username = existing_users[0]
        while random_username in existing_users:
            random_username = "Auto_username" + ''.join(random.choices(string.digits, k=3))
        password = "1234"
        # Writing the new random username to logger, and also the const password
        logger.info(f"new random username created: username: {random_username}, password: {password}")
        # Copying the new random 'username' and 'password' into a local 'users.txt' file
        try:
            with open("users.txt", "a") as users_file:
                users_file.write(f"\nusername: {random_username}, password: {password}")
        except Exception as e:
            logger.error(e, "\nAdding the new random username credentials to 'users.txt' file failed")

        # Continue populating the SignUp form and signing-up a new user
        driver.find_element(By.ID, "firstname").send_keys("QAAuto_FirstName")
        driver.find_element(By.ID, "lastname").send_keys("QAAuto_LastName")
        driver.find_element(By.ID, "username").send_keys(random_username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "confirm_password").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
        alert_success = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success").text
        # Validate that new user successfully signed-up
        logger.info("Validate that new user successfully signed-up")
        assert ("Welcome, QAAuto_FirstName QAAuto_LastName and thanks fo"
                "r registration!") in alert_success, logger("Failed to SignUp a new user")
        logger.info("Scenario_1 Passed")

        driver.close()
        print("Scenario_1 Finished")

    """Scenario_2."""
    @pytest.mark.regression
    @pytest.mark.functional
    def test_002_signup_existing_user_shall_rejected(self, chrome_driver_setup, logger_setup):
        """
        Test Description: SignUp using an existing user in DB.
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_2 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        nav_links = driver.find_elements(By.XPATH, "//nav/a")
        # Redirection to 'SignUp' page
        for link in nav_links:
            if "register" in link.get_attribute("href"):
                link.click()
        logger.info("redirect to 'register page'")
        # selecting any existing 'username' from DB
        existing_usernames = json.loads(requests.get("https://carsphere.onrender.com/get-users").text)
        # print(existing_usernames)
        username = ''
        logger.info(type(existing_usernames))
        for name in existing_usernames:
            if name != 'admin':
                username = name
                break
        logger.info(username)
        password = "1235"
        # Continue populating the Signup form and trying to signing-up an existing username
        driver.find_element(By.ID, "firstname").send_keys("QAAuto_FirstName")
        driver.find_element(By.ID, "lastname").send_keys("QAAuto_LastName")
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "confirm_password").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
        alert_danger = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger").text
        # Validate that signing-up of an existing user successfully rejected
        logger.info("Validate that signing-up of an existing user successfully rejected")
        assert (f"Username '{username}' already exist, "
                f"please try another username.") in alert_danger, ("SignUp an new user shall not be "
                                                                    "allowed. Expected to 'blocking this behavior'")
        logger.info("Scenario_2 Passed")

        driver.close()
        print("Scenario_2 Finished")


    """Scenario_3."""
    @pytest.mark.regression
    @pytest.mark.functional
    def test_003_mismatch_confirm_password(self, chrome_driver_setup, logger_setup):
        """
        Test Description:
        Test user signup when password and confirm password do not match.
        Ensures the system blocks registration and displays an appropriate error message.
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_3 Begin")
        driver.get("https://carsphere.onrender.com")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/register']").click()
        # Generating a new random 'username' and checking that it do not already included in the DB
        # First: getting a list of all existing usernames from DB
        response = requests.get("https://carsphere.onrender.com/get-users")
        existing_users = response.text
        logger.debug(f"getting all existing users from DB:\n{existing_users}")
        # Second: Generating a new random username and checking that it is not exist already in DB
        random_username = existing_users[0]
        while random_username in existing_users:
            random_username = "Auto_username" + ''.join(random.choices(string.digits, k=3))
        # Preparing not matches passwords for 'Password' and 'Confirm password' fields
        for_password_input = "1234"
        for_confirma_password_input = "8888"
        # Writing the new random username to logger, and also the const password
        logger.info(f"new random username created: username:"
                    f" {random_username}, password: {for_password_input}, confirm_password: {for_confirma_password_input}")
        # Copying the new random 'username' and 'password' into a local 'users.txt' file
        try:
            with open("users.txt", "a") as users_file:
                users_file.write(f"\nusername: {random_username}, "
                                 f"password: {for_password_input}, conform_password: {for_confirma_password_input}")
        except Exception as e:
            logger.error(e, "\nAdding the new random username credentials to 'users.txt' file failed")
        # Continue populating the SignUp form and signing-up a new user
        driver.find_element(By.ID, "firstname").send_keys("QAAuto_FirstName")
        driver.find_element(By.ID, "lastname").send_keys("QAAuto_LastName")
        driver.find_element(By.ID, "username").send_keys(random_username)
        driver.find_element(By.ID, "password").send_keys(for_password_input)
        driver.find_element(By.ID, "confirm_password").send_keys(for_confirma_password_input)
        driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
        confirm_password_alert = driver.find_element(By.ID, "confirm_pass")
        confirm_password_alert_expected_color = "rgba(255, 0, 0, 1)"
        # Validate that registration rejected when 'Password' and 'Confirm Password' values are not identical
        logger.info("Validate that registration rejected when 'Password' and 'Confirm Password' values are not identical")
        try:
            assert (confirm_password_alert.text == "Passwords are not match"
                    and confirm_password_alert.value_of_css_property("color") == confirm_password_alert_expected_color)
            logger.info("Scenario_3 Passed")
        except AssertionError as e:
            logger.info("Scenario_3 Failed")
            raise AssertionError(e)

        driver.close()
        print("Scenario_3 Finished")


@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestLoginUser:
    """This class groups the 'Login' testing actions"""

    """Scenario_4."""
    @pytest.mark.system
    @pytest.mark.functional
    def test_004_admin_login_valid_credentials(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Login using 'admin' valid credentials
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_4 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        actual_login_success_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-success']").text
        expected_login_success_message = "Welcome, Administrator Manager!"
        # Validate 'admin' user success with valid credentials
        logger.info("Validate 'admin' user success with valid credentials")
        assert actual_login_success_message == expected_login_success_message, \
            f"Scenario_4 Failed.\nExpected message '{expected_login_success_message}' \
            got '{actual_login_success_message}'"
        logger.info("Scenario_4 Passed")

        driver.close()
        print("Scenario_4 Finished")


    """Scenario_5"""
    @pytest.mark.system
    @pytest.mark.functional
    def test_005_admin_login_invalid_credentials(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Login using 'admin' user with invalid credentials
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_5 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("1234")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        actual_login_unsuccessful_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-danger']").text
        expected_login_success_message = "Login Unsuccessful. Please check username and password"
        # Validate that login rejected for 'admin' user with invalid credentials
        logger.info("Validate that login rejected for 'admin' user with invalid credentials")
        assert actual_login_unsuccessful_message == expected_login_success_message, \
            f"Scenario_5 Failed.\nExpected message '{expected_login_success_message}' \
            got '{actual_login_unsuccessful_message}'"
        logger.info("Scenario_5 Passed")

        driver.close()
        print("Scenario_5 Finished")


    """Scenario_6"""
    @pytest.mark.sanity
    @pytest.mark.system
    @pytest.mark.functional
    def test_006_non_admin_login_valid_credentials(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Login using 'non admin' user with valid credentials
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_6 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        actual_login_success_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-success']").text
        expected_login_success_message = "Welcome, user3 user3!"
        # Validate login success for 'non admin' user with valid credentials
        logger.info("Validate login success for 'non admin' user with valid credentials")
        assert actual_login_success_message == expected_login_success_message, \
            f"Scenario_6 Failed.\nExpected message '{expected_login_success_message}' \
            got '{actual_login_success_message}'"
        logger.info("Scenario_6 Passed")

        driver.close()
        print("Scenario_6 Finished")


    """Scenario_7"""
    @pytest.mark.system
    @pytest.mark.functional
    def test_007_non_admin_login_invalid_credentials(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Login using 'non admin' user with invalid credentials
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_7 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        actual_login_unsuccessful_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-danger']").text
        expected_login_unsuccessful_message = "Login Unsuccessful. Please check username and password"
        # Validate login rejected for 'non admin' user with invalid credentials
        logger.info("Validate login rejected for 'non admin' user with invalid credentials")
        assert actual_login_unsuccessful_message == expected_login_unsuccessful_message, \
            f"Scenario_6 Failed.\nExpected message '{expected_login_unsuccessful_message}' \
            got '{actual_login_unsuccessful_message}'"
        logger.info("Scenario_7 Passed")

        driver.close()
        print("Scenario_7 Finished")

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestLogoutUsers:
    """This class groups the 'Logout' testing for both 'admin' and 'non admin' users"""

    """Scenario_8"""
    @pytest.mark.regression
    @pytest.mark.functional
    def test_008_logout_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Logout 'admin' user
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_8 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        driver.find_element(By.XPATH, "//nav/a[@href='/logout']").click()
        logout_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        # Validate logout success for 'admin' user
        logger.info("Validate logout success for 'admin' user")
        assert logout_success_message.text == "You have been logged out.", "'admin' user logout failed"
        logger.info("'admin user logout success")
        logger.info("'Scenario_14 Passed")

        driver.close()
        print("Scenario_8 Finished")

    """Scenario_9"""
    @pytest.mark.regression
    @pytest.mark.functional
    def test_009_logout_non_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Logout 'non admin' user
        :param chrome_driver_setup: initializing the webdriver
        :param logger_setup: initializing the logger
        :return: None
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_9 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        driver.find_element(By.XPATH, "//nav/a[@href='/logout']").click()
        logout_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        # Validate logout success for 'non admin' user
        logger.info("Validate logout success for 'non admin' user")
        assert logout_success_message.text == "You have been logged out.", "'non admin' user logout failed"
        logger.info("'non admin user logout success")
        logger.info("'Scenario_15 Passed")

        driver.close()
        print("Scenario_9 Finished")
