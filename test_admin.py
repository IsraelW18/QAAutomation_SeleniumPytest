""" This module includes testing for 'admin' special actions """
import os.path
import string
import random
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestAdminActionsPermissions:
    """ This class groups the admin special actions 'permissions' """

    """Scenario_10"""
    @pytest.mark.functionalAdminTools
    def test_010_add_new_car_action_displayed_for_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: 'Add New Car' button shall be available only when login using 'admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_10 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # Validate that 'Add New Car' option/button displayed for 'admin' user
        logger.info("Validate that 'Add New Car' option/button displayed for 'admin' user")
        try:
            add_new_car_button = driver.find_element(By.XPATH, "//nav/a[@href='/add_car']")
            assert add_new_car_button.text == "Add New Car"
            logger.info("Scenario_10 Passed")
        except NoSuchElementException as e:
            logger.error("Expected 'Add New Car button', but element not found")
            raise NoSuchElementException("Scenario_10 Failed")

        driver.close()
        print("Scenario_10 Finished")

    """Scenario_9"""
    @pytest.mark.functionalAdminTools
    def test_011_delete_action_displayed_for_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: 'Delete' button shall be available only when login using 'admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_11 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # Validate that 'Delete' item option displayed for 'admin' user
        logger.info("Validate that 'Delete' item option displayed for 'admin' user")
        test_passed = [True]
        try:
            delete_car_buttons = driver.find_elements(By.XPATH, "//div[@class='car-item']/form/button[@class='btn btn-danger']")
            for delete_btn in delete_car_buttons:
                assert delete_btn.text == "Delete", test_passed.append(False)
                logger.info(f"Deleted button exist for Car item No.'{delete_car_buttons.index(delete_btn)}'")
                test_passed.append(True)
        except AssertionError as e:
            logger.error("Expected 'Delete' button, but element not found")
            raise AssertionError(e)

        if test_passed:
            logger.info("Scenario_11 Passed")
        else:
            logger.info("Scenario_11 Failed")
        driver.close()
        print("Scenario_11 Finished")

    """Scenario_12"""
    @pytest.mark.functionalAdminTools
    def test_012_add_new_car_action_hidden_for_non_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: 'Add New Car' button is hidden for 'non admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_12 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        add_new_car_button_text = driver.find_elements(By.XPATH, "//nav/a[@href='/add_car']")
        # Validate that 'Add New Car' option/button is hidden for 'non admin' user
        logger.info("Validate that 'Add New Car' option/button is hidden for 'non admin' user")
        try:
            assert add_new_car_button_text != "Add New Car", \
                "Element 'Add New Car' button is visible for 'non admin users'. Expected to be hidden"
            logger.info("Scenario_12 Passed")
        except AssertionError as e:
            raise AssertionError("Scenario_12 Failed")

        driver.close()
        print("Scenario_12 Finished")

    """Scenario_13"""
    @pytest.mark.functionalAdminTools
    def test_013_delete_action_hidden_for_non_admin(self, chrome_driver_setup, logger_setup):
        """
        Test Description: 'Delete' button is hidden for 'non admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_13 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        delete_car_buttons = driver.find_elements(By.XPATH,
                                                  "//div[@class='car-item']/form/button[@class='btn btn-danger']")
        # Validate that 'Delete' option/button is hidden for 'non admin' user
        logger.info("Validate that 'Delete' option/button is hidden for 'non admin' user")
        try:
            assert delete_car_buttons == [], "Expected 'Delete' buttons to be hidden for 'non admin' users. But element is visible"
            logger.info("scenario_13 Passed")
        except AssertionError as e:
            logger.error(f"{e}, Scenario_13 Failed:")
            raise AssertionError(e)

        driver.close()
        print("Scenario_13 Finished")

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestAdminActions:
    """This class groups the 'admin special actions' using 'admin' user"""

    """Scenario_14"""
    @pytest.mark.functionalAdminTools
    def test_014_admin_action_add_new_car(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Adding a new Car to CarSphere catalog using 'admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_14 Begin")
        driver. get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        driver.find_element(By.XPATH, "//nav/a[@href='/add_car']").click()
        # Generate a random Car maker
        make_input = "Auto Make Tesla" + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.XPATH, "//input[@id='make']").send_keys(make_input)
        # Generate a random Car model
        model_input = "Auto Model Y" + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.XPATH, "//input[@id='model']").send_keys(model_input)
        # Generate a random Car Year to be selected in the 'Year' combobox
        years_combobox_elements = driver.find_elements(By.XPATH, "//select/option")
        random_index = random.randint(1, 18)
        for year in years_combobox_elements:
            if years_combobox_elements.index(year) == random_index:
                year.click()
                break
        # Generate a random Director
        director_input = "Auto Director " + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.XPATH, "//input[@id='director']").send_keys(director_input)
        # Generate a random Main Settings
        main_settings_input = "Auto Main Settings " + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.ID, "main_settings").send_keys(main_settings_input)
        # Generate a random Description
        description_input = "Auto Description " + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.XPATH, "//div/textarea[@name='description']").send_keys(description_input)
        # Selecting an image from PC
        file_picture_input = driver.find_element(By.XPATH, "//input[@id='image_file']")
        file_picture_input.send_keys(os.path.abspath(".\\test_images\\AutoTestCar.jpg"))
        driver.find_element(By.XPATH, "//input[@id='submit']").click()
        add_car_success_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-success']").text
        # Validate that new car is added to CarSphere catalog when logged-in with 'admin user
        logger.info("Validate that new car is added to CarSphere catalog when logged-in with 'admin user")
        assert (add_car_success_message ==
                f"Car {make_input} {model_input} added successfully!"), ("Failed to add"
                                                                         " new Car to Catalog\nScenario_14 Failed")
        logger.info("New Car successfully added to CarSphere Catalog")
        logger.info("Scenario_14 Passed")

        driver.close()
        print("Scenario_14 Finished")

    """Scenario_15"""
    @pytest.mark.functionalAdminTools
    def test_015_admin_action_delete_car(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Delete a Car from CarSphere catalog using 'admin' user
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_15 Begin")
        driver. get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        cars_element_list = driver.find_elements(By.XPATH, "//div/div[@class='car-item']/form/button")
        cars_element_list[-1].click()
        delete_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        # Validate that existing car is deleted from CarSphere catalog when logged-in with 'admin' user
        logger.info("Validate that existing car is deleted from CarSphere catalog when logged-in with 'admin' user")
        assert delete_success_message.text == "Car deleted successfully!", \
            "Car do not deleted. Expected - car shall be deleted\nScenario 15 Failed"
        logger.info("Car successfully deleted from CarSphere catalog")
        logger.info("Scenario_15 Passed")

        driver.close()
        print("Scenario_15 Finished")

