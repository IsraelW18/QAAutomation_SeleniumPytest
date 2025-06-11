# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.XPATH, "//div/input[@id='username']")
    PASSWORD_INPUT = (By.XPATH, "//div/input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//form/button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://carsphere.onrender.com/login"

    def navigate_to(self):

        self.driver.get(self.url)

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()