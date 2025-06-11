from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import requests

class RegisterPage(BasePage):
    NAV_LINKS = (By.XPATH, "//nav/a")
    FIRST_NAME = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='lastname']")
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='confirm_password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Sign Up']")

    def navigate_to_register_page(self, driver):
        links = self.find_elements(*self.NAV_LINKS)
        for link in links:
            if "register" in link.get_attribute("href"):
                link.click()
                break

    def get_user_from_api(self):
        pass

    def fill_registration_form(self, first_name, last_name, username, password, confirm_password):
        self.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.find_element(*self.LAST_NAME).send_keys(last_name)
        self.find_element(*self.USERNAME).send_keys(username)
        self.find_element(*self.PASSWORD).send_keys(password)
        self.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*self.SUBMIT_BUTTON).click()
