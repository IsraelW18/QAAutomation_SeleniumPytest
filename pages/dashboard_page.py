# pages/dashboard_page.py
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locators
    ADD_NEW_CAR_BUTTON = (By.XPATH, "//nav/a[@href='/add_car']")
    DELETE_CAR_BUTTONS = (By.XPATH, "//div[@class='car-item']/form/button[@class='btn btn-danger']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success")
    
    # Add Car Form Locators
    MAKE_INPUT = (By.XPATH, "//input[@id='make']")
    MODEL_INPUT = (By.XPATH, "//input[@id='model']")
    YEAR_SELECT = (By.XPATH, "//select/option")
    DIRECTOR_INPUT = (By.XPATH, "//input[@id='director']")
    MAIN_SETTINGS_INPUT = (By.ID, "main_settings")
    DESCRIPTION_INPUT = (By.XPATH, "//div/textarea[@name='description']")
    IMAGE_INPUT = (By.XPATH, "//input[@id='image_file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@id='submit']")
    # ADD_CAR_SUCCESS_MESSAGE = (By.XPATH, "//div/div[@class='alert alert-success']")
    # DELETE_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-success")

    def is_add_new_car_visible(self):
        return self.is_element_visible(*self.ADD_NEW_CAR_BUTTON)

    def are_delete_buttons_visible(self):
        try:
            delete_buttons = self.find_elements(*self.DELETE_CAR_BUTTONS)
            return len(delete_buttons) > 0
        except TimeoutException:
            return False

    def add_new_car(self, make, model, year, director, settings, description, image_path):
        self.find_element(*self.MAKE_INPUT).send_keys(make)
        self.find_element(*self.MODEL_INPUT).send_keys(model)
        # Select year from dropdown
        year.click()
        self.find_element(*self.DIRECTOR_INPUT).send_keys(director)
        self.find_element(*self.MAIN_SETTINGS_INPUT).send_keys(settings)
        self.find_element(*self.DESCRIPTION_INPUT).send_keys(description)
        self.find_element(*self.IMAGE_INPUT).send_keys(image_path)
        self.find_element(*self.SUBMIT_BUTTON).click()
        return self.get_success_message() == f"Car {make} {model} added successfully!"

    def delete_last_car(self):
        delete_buttons = self.find_elements(*self.DELETE_CAR_BUTTONS)
        if len(delete_buttons) > 6:
            try:
                delete_buttons[-1].click()
                return self.get_success_message() == "Car deleted successfully!"
            except TimeoutException:
                return False
        return False

    def get_success_message(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text

    def navigate_to_add_new_car_form(self):
        self.find_element(*self.ADD_NEW_CAR_BUTTON).click()