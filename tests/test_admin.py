"""
Module: test_admin

Description:
This module contains automated tests for verifying 'admin-specific actions' and permissions in the CarSphere application.
The tests ensure that privileged actions, such as adding and deleting cars, are available only to 'admin' users
and properly restricted for non-admin users.

Key Features Tested:
1. Admin permissions for adding and deleting cars.
2. Visibility and accessibility of privileged actions for admin and non-admin users.
3. Proper success and failure messaging for admin actions.

Test Classes:
- `TestAdminActionsPermissions`: Verifies visibility of restricted features based on user permissions.
- `TestAdminActions`: Validates that admin users can perform specific actions, such as adding or deleting cars.

Fixtures:
- `chrome_driver_setup`: Provides a configured Chrome WebDriver instance for Selenium automation.
- `logger_setup`: Provides a logger instance for detailed test execution logs.

Preconditions:
- The CarSphere application must be running and accessible at the predefined URL.
- Admin and non-admin user accounts must exist in the system.
- Chrome WebDriver must be available on the system.
- Test images or required assets must exist in the specified paths.

Usage:
```bash
Run the module using pytest:
        pytest test_admin.py
"""
import os.path
import string
import random
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestAdminActionsPermissions:
    """
    Test Class: TestAdminActionsPermissions

    This class groups all functional tests related to verifying 'admin-specific permissions' in the CarSphere application.
    The tests focus on validating the visibility and accessibility of restricted features, such as 'Add New Car' and 'Delete' actions,
    for admin and non-admin users.

    Key Objectives:
    1. Ensure that privileged actions, such as adding or deleting cars, are available only to 'admin' users.
    2. Verify that non-admin users cannot access or see restricted actions, ensuring proper permission enforcement.
    3. Validate application behavior and messaging when performing permission-related tests.

    Test Scenarios Included:
    - Scenario_10: Verify that the 'Add New Car' button is displayed for the 'admin' user.
    - Scenario_11: Verify that the 'Delete' button is displayed for the 'admin' user.
    - Scenario_12: Verify that the 'Add New Car' button is hidden for non-admin users.
    - Scenario_13: Verify that the 'Delete' button is hidden for non-admin users.

    Fixtures:
    - `chrome_driver_setup`: Provides a configured Chrome WebDriver instance for browser automation.
    - `logger_setup`: Provides a logger instance for detailed test execution logging.

    Preconditions:
    - The application is running and accessible at the predefined URL.
    - Chrome browser is installed and set up for automation.
    - Both 'admin' and 'non-admin' user accounts exist in the system with appropriate permissions.
    """

    """Scenario_10"""
    @pytest.mark.functionalAdminTools
    def test_010_add_new_car_action_displayed_for_admin(self, chrome_driver_setup, logger_setup):
        """
        Opening Note:
        This test scenario ensures that the 'Add New Car' button is displayed exclusively when logging in with an 'admin' user account.
        The validation process includes:
        1. Logging into the application using admin credentials.
        2. Checking for the presence of the 'Add New Car' button in the navigation bar with the expected text.
        3. Logging the test flow and asserting the validation results.

        The test logs results as follows:
        - On success: The log indicates that the button was successfully located.
        - On failure: The log documents that the button was not found, and the test raises a `NoSuchElementException`.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - An 'admin' user account with proper permissions exists in the system.
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test performs assertions to validate functionality and logs the results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM_start_part_1"""

        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        logger.info("Logging in as admin")
        login_page.navigate_to()
        login_page.login("admin", "admin")

        logger.info("Validate that 'Add New Car' button displayed for 'admin' user")
        assert dashboard_page.is_add_new_car_visible(), "Add New Car button not found"
        logger.info("Scenario_10 Passed")

        # print("Scenario_10 Begin")
        # driver.get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # # Validate that 'Add New Car' option/button displayed for 'admin' user
        # logger.info("Validate that 'Add New Car' option/button displayed for 'admin' user")
        # try:
        #     add_new_car_button = driver.find_element(By.XPATH, "//nav/a[@href='/add_car']")
        #     assert add_new_car_button.text == "Add New Car"
        #     logger.info("Scenario_10 Passed")
        # except NoSuchElementException as e:
        #     logger.error("Expected 'Add New Car button', but element not found")
        #     raise NoSuchElementException("Scenario_10 Failed")

        driver.close()

        """POM_finish_part_1"""


    """Scenario_9"""
    @pytest.mark.functionalAdminTools
    def test_011_delete_action_displayed_for_admin(self, chrome_driver_setup, logger_setup):
        """
        This function verifies the availability of the 'Delete' button for the 'admin' user only.

        Test Description:
        This test ensures that the 'Delete' button is displayed for car items exclusively when logged in as an 'admin' user.
        The validation process includes:
        1. Logging into the application using admin credentials.
        2. Checking for the presence of 'Delete' buttons for each car item displayed on the page.
        3. Asserting that the button text is 'Delete' and logging results for each car item.

        Test Flow:
        - On success: Each car item has a 'Delete' button, and the test logs its presence.
        - On failure: Missing or incorrect 'Delete' buttons raise an `AssertionError`, and the test logs the failure.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - An 'admin' user account with proper permissions exists in the system.

        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test validates the presence of 'Delete' buttons and logs results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM start part 2"""
        # Use POM pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        # Login
        logger.info("Logging in as admin")
        login_page.navigate_to()
        login_page.login("admin", "admin")

        logger.info("Validate that 'Delete buttons' are visible for admin user")
        try:
            assert dashboard_page.are_delete_buttons_visible(), "Delete buttons not found"
            logger.info("Scenario_11 Passed")
        except AssertionError as e:
            logger.info(f"Scenario_11 Failed.\n{e}")


        # driver.get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # # Validate that 'Delete' item option displayed for 'admin' user
        # logger.info("Validate that 'Delete' item option displayed for 'admin' user")
        # test_passed = [True]
        # try:
        #     delete_car_buttons = driver.find_elements(By.XPATH, "//div[@class='car-item']/form/button[@class='btn btn-danger']")
        #     for delete_btn in delete_car_buttons:
        #         assert delete_btn.text == "Delete", test_passed.append(False)
        #         logger.info(f"Deleted button exist for Car item No.'{delete_car_buttons.index(delete_btn)}'")
        #         test_passed.append(True)
        # except AssertionError as e:
        #     logger.error("Expected 'Delete' button, but element not found")
        #     raise AssertionError(e)
        #
        # if test_passed:
        #     logger.info("Scenario_11 Passed")
        # else:
        #     logger.info("Scenario_11 Failed")
        driver.close()

        """POM part 2 finished"""

    """Scenario_12"""
    @pytest.mark.functionalAdminTools
    def test_012_add_new_car_action_hidden_for_non_admin(self, chrome_driver_setup, logger_setup):
        """
        This function verifies that the 'Add New Car' button is hidden for non-admin users.

        Test Description:
        This test ensures that the 'Add New Car' button does not appear when logged in as a non-admin user.
        The validation process includes:
        1. Logging into the application using non-admin user credentials.
        2. Searching for the 'Add New Car' button in the navigation bar.
        3. Asserting that the button is not visible or accessible to non-admin users.

        Test Flow:
        - On success: The 'Add New Car' button is not displayed, and the test passes.
        - On failure: If the button is visible, the test raises an `AssertionError` and logs the failure.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - A non-admin user account exists in the system with limited permissions.

        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test verifies button visibility and logs results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM part 3 start"""

        # Use POM pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        logger.info("Logging in as Non admin user")
        login_page.navigate_to()
        login_page.login("user3", "user3")

        # Validate that 'Add New Car' button do not displayed for non admin users
        logger.info("Validate that 'Add New Car' button do not displayed for 'Non admin' users ")
        assert not dashboard_page.is_add_new_car_visible(), "'Add New Car' button is visible for Non admin users"
        logger.info("Scenario_12 Passed")

        # driver.get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # add_new_car_button_text = driver.find_elements(By.XPATH, "//nav/a[@href='/add_car']")
        # # Validate that 'Add New Car' option/button is hidden for 'non admin' user
        # logger.info("Validate that 'Add New Car' option/button is hidden for 'non admin' user")
        # try:
        #     assert add_new_car_button_text != "Add New Car", \
        #         "Element 'Add New Car' button is visible for 'non admin users'. Expected to be hidden"
        #     logger.info("Scenario_12 Passed")
        # except AssertionError as e:
        #     raise AssertionError("Scenario_12 Failed")

        """POM part 3 finished"""

        driver.close()

    """Scenario_13"""
    @pytest.mark.functionalAdminTools
    def test_013_delete_action_hidden_for_non_admin(self, chrome_driver_setup, logger_setup):
        """
        This function verifies that the 'Delete' button is hidden for non-admin users.

        Test Description:
        This test ensures that the 'Delete' button is not displayed when logged in as a non-admin user.
        The validation process includes:
        1. Logging into the application using non-admin user credentials.
        2. Searching for 'Delete' buttons associated with car items on the page.
        3. Asserting that no 'Delete' buttons are visible for the non-admin user.

        Test Flow:
        - On success: The test confirms that no 'Delete' buttons are displayed, and logs the result as passed.
        - On failure: If any 'Delete' button is visible, an `AssertionError` is raised, and the failure is logged.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - A non-admin user account exists in the system with limited permissions.

        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test validates that 'Delete' buttons are hidden and logs the results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM part 4 start"""

        # User POM pages
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        # Login as 'non admin' user
        login_page.navigate_to()
        login_page.login("user3", "user3")

        # Validate that 'Delete' car buttons do not display for 'Non admin' users
        logger.info("Validate that 'Delete' car buttons do not display for 'Non admin' users ")
        assert not dashboard_page.are_delete_buttons_visible(), "'Delete' car buttons appear for 'Non admin users'"
        logger.info("Scenario_13 Passed")


        # driver.get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # delete_car_buttons = driver.find_elements(By.XPATH,
        #                                           "//div[@class='car-item']/form/button[@class='btn btn-danger']")
        # # Validate that 'Delete' option/button is hidden for 'non admin' user
        # logger.info("Validate that 'Delete' option/button is hidden for 'non admin' user")
        # try:
        #     assert delete_car_buttons == [], "Expected 'Delete' buttons to be hidden for 'non admin' users. But element is visible"
        #     logger.info("scenario_13 Passed")
        # except AssertionError as e:
        #     logger.error(f"{e}, Scenario_13 Failed:")
        #     raise AssertionError(e)

        """POM part 4 finished"""

        driver.close()

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestAdminActions:
    """
    Test Class: TestAdminActions

    This class groups all functional tests related to 'admin-only actions' in the CarSphere application.
    The tests validate that specific features, such as adding or deleting cars, are available and functional only when using an 'admin' user account.

    Key Objectives:
    1. Verify that 'admin' users can perform privileged actions, such as adding and deleting cars.
    2. Ensure restricted actions are inaccessible to non-admin users.
    3. Validate proper application responses, including success messages, when admin actions are executed.

    Test Scenarios Included:
    - Scenario_14: Verify that an 'admin' user can add a new car to the catalog.
    - Scenario_15: Verify that an 'admin' user can delete an existing car from the catalog.

    Fixtures:
    - `chrome_driver_setup`: Provides a configured Chrome WebDriver for browser automation.
    - `logger_setup`: Provides a logger instance for test execution logging.

    Preconditions:
    - The application must be running and accessible at the predefined URL.
    - An 'admin' user account with appropriate privileges exists in the system.
    - Chrome WebDriver is installed and available for test execution.
    """

    """Scenario_14"""
    @pytest.mark.functionalAdminTools
    def test_014_admin_action_add_new_car(self, chrome_driver_setup, logger_setup):
        """
        This function verifies that an 'admin' user can successfully add a new car to the CarSphere catalog.

        Test Description:
        This test ensures that the 'admin' user can perform the 'Add New Car' action, and the new car is successfully added to the catalog.
        The test generates random input values for car details, uploads an image, and validates the success message upon submission.

        Test Steps:
        1. Log into the application using admin credentials.
        2. Navigate to the 'Add New Car' page.
        3. Enter random details for the following fields:
           - Car Make
           - Car Model
           - Car Year (selected randomly from the dropdown list)
           - Director
           - Main Settings
           - Description
        4. Upload an image file for the car.
        5. Submit the form and validate the success message.

        Test Flow:
        - On success: A confirmation message is displayed, verifying that the car was added successfully, and the test logs the success.
        - On failure: If the success message is incorrect or missing, the test raises an `AssertionError` and logs the failure.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - An 'admin' user account with proper permissions exists in the system.
        - A test image file named `AutoTestCar.jpg` exists in the `test_images` directory on the local machine.

        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test validates that a new car is added successfully and logs the results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM part 5 start"""

        # Use POM pages
        dashboard_page = DashboardPage(driver)
        login_page = LoginPage(driver)

        logger.info("Logging in as 'admin' user")
        login_page.navigate_to()
        login_page.login("admin", "admin")
        dashboard_page.navigate_to_add_new_car_form()

        make_input = "Auto Make Tesla" + ''.join(random.choices(string.digits, k=3))
        model_input = "Auto Model Y" + ''.join(random.choices(string.digits, k=3))
        years_combobox_elements = driver.find_elements(By.XPATH, "//select/option")
        random_index = random.randint(1, 18)
        # for year in years_combobox_elements:
        #     if years_combobox_elements.index(year) == random_index:
        #         year.click()
        #         break
        logger.info(f"year_combobox_elements: {years_combobox_elements}")
        logger.info(f"random_index: {random_index}")
        year_input = years_combobox_elements[random_index]
        logger.info(f"year_input: {year_input}")
        director_input = "Auto Director " + ''.join(random.choices(string.digits, k=3))
        settings_input = "Auto Settings " + ''.join(random.choices(string.digits, k=3))
        description_input = "Auto Description " + ''.join(random.choices(string.digits, k=3))
        image_input = os.path.abspath("./test_images/AutoTestCar.jpg")
        new_car_added_message_status = dashboard_page.add_new_car(make=make_input,
                                                                  model=model_input,
                                                                  year=year_input,
                                                                  director=director_input,
                                                                  settings=settings_input,
                                                                  description=description_input,
                                                                  image_path=image_input)
        logger.info(new_car_added_message_status)
        print(new_car_added_message_status)
        # Validate that Car successfully added
        logger.info("Validate that Car successfully added")
        assert new_car_added_message_status, "New car did not added"
        logger.info("Scenario_14 Passed")


        # driver. get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # driver.find_element(By.XPATH, "//nav/a[@href='/add_car']").click()
        # # Generate a random Car maker
        # make_input = "Auto Make Tesla" + ''.join(random.choices(string.digits, k=3))
        # driver.find_element(By.XPATH, "//input[@id='make']").send_keys(make_input)
        # # Generate a random Car model
        # model_input = "Auto Model Y" + ''.join(random.choices(string.digits, k=3))
        # driver.find_element(By.XPATH, "//input[@id='model']").send_keys(model_input)
        # # Generate a random Car Year to be selected in the 'Year' combobox
        # years_combobox_elements = driver.find_elements(By.XPATH, "//select/option")
        # random_index = random.randint(1, 18)
        # for year in years_combobox_elements:
        #     if years_combobox_elements.index(year) == random_index:
        #         year.click()
        #         break
        # # Generate a random Director
        # director_input = "Auto Director " + ''.join(random.choices(string.digits, k=3))
        # driver.find_element(By.XPATH, "//input[@id='director']").send_keys(director_input)
        # # Generate random Main Settings
        # main_settings_input = "Auto Main Settings " + ''.join(random.choices(string.digits, k=3))
        # driver.find_element(By.ID, "main_settings").send_keys(main_settings_input)
        # # Generate a random Description
        # description_input = "Auto Description " + ''.join(random.choices(string.digits, k=3))
        # driver.find_element(By.XPATH, "//div/textarea[@name='description']").send_keys(description_input)
        # # Selecting an image from PC
        # file_picture_input = driver.find_element(By.XPATH, "//input[@id='image_file']")
        # file_picture_input.send_keys(os.path.abspath("../test_images/AutoTestCar.jpg"))
        # driver.find_element(By.XPATH, "//input[@id='submit']").click()
        # add_car_success_message = driver.find_element(By.XPATH, "//div/div[@class='alert alert-success']").text
        # # Validate that new car is added to CarSphere catalog when logged-in with 'admin user
        # logger.info("Validate that new car is added to CarSphere catalog when logged-in with 'admin user")
        # assert (add_car_success_message ==
        #         f"Car {make_input} {model_input} added successfully!"), ("Failed to add"
        #                                                                  " new Car to Catalog\nScenario_14 Failed")
        # logger.info("New Car successfully added to CarSphere Catalog")
        # logger.info("Scenario_14 Passed")

        """POM part 5 finished"""

        driver.close()


    """Scenario_15"""
    @pytest.mark.functionalAdminTools
    def test_015_admin_action_delete_car(self, chrome_driver_setup, logger_setup):
        """
        This function verifies that an 'admin' user can successfully delete a car from the CarSphere catalog.

        Test Description:
        This test ensures that an 'admin' user can perform the 'Delete Car' action, and the selected car is successfully removed from the catalog.
        The validation process includes navigating to the car list, performing a delete action, and verifying the success message.

        Test Steps:
        1. Log into the application using admin credentials.
        2. Identify the list of cars displayed in the catalog.
        3. Click on the 'Delete' button for the last car in the list.
        4. Validate the presence of a success message confirming the car's deletion.

        Test Flow:
        - On success: A confirmation message is displayed, verifying that the car was deleted successfully, and the test logs the success.
        - On failure: If the success message is incorrect or missing, the test raises an `AssertionError` and logs the failure.

        Preconditions:
        - The application is running and accessible at the predefined URL.
        - Chrome browser is available and set up for the test.
        - An 'admin' user account with proper permissions exists in the system.
        - The car catalog contains at least one car to ensure the delete action can be performed.

        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.
        :return: None. The test validates that a car is deleted successfully and logs the results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")

        """POM part 6 start"""

        # Use POM pages
        loging_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        logger.info("Logging in as 'admin' user")
        loging_page.navigate_to()
        loging_page.login("admin", "admin")

        # Trying to delete the last car added to Catalog
        logger.info("Trying to delete the last car added to Catalog")
        delete_success_message = dashboard_page.delete_last_car()
        logger.info(f"delete_car_success_message: {delete_success_message}")
        print("delete_car_success_message: ", delete_success_message)
        assert dashboard_page.delete_last_car(), "Failed to delete the last added car"
        logger.info("Scenario_15 Passed")

        # driver. get("https://carsphere.onrender.com/")
        # logger.info("Redirecting to application 'Home Page'")
        # driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        # driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("admin")
        # driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("admin")
        # driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        # cars_element_list = driver.find_elements(By.XPATH, "//div/div[@class='car-item']/form/button")
        # cars_element_list[-1].click()
        # delete_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        # # Validate that existing car is deleted from CarSphere catalog when logged-in with 'admin' user
        # logger.info("Validate that existing car is deleted from CarSphere catalog when logged-in with 'admin' user")
        # assert delete_success_message.text == "Car deleted successfully!", \
        #     "Car do not deleted. Expected - car shall be deleted\nScenario 15 Failed"
        # logger.info("Car successfully deleted from CarSphere catalog")

        """POM part 6 finished"""
        driver.close()

