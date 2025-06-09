"""
Module: test_gallery

Description:
This module contains automated test scenarios for the CarSphere application, focusing on:
1. GUI elements and redirection testing for the CarSphere gallery.
2. User reviews functionality, including manual reviews and AI-generated reviews.

Key Areas Tested:
- **Main Page Background**: Ensures that the website background image is correct.
- **Branding and Social Links**: Verifies proper URL redirection for branding and LinkedIn icons.
- **User Reviews**: Tests user ability to add manual reviews and validate the AI-generated reviews functionality.

Test Classes:
1. `TestGUIAndRedirections`:
   - Tests GUI components and icon-based redirections (Scenarios 16-18).
2. `TestReviews`:
   - Tests user manual reviews and AI-generated reviews submission (Scenarios 19-20).

Test Scenarios:
- **Scenario_16**: Validate main page background image.
- **Scenario_17**: Validate the CarSphere branding icon redirection URL.
- **Scenario_18**: Validate LinkedIn icon redirection.
- **Scenario_19**: Test user manual review submission and its visibility.
- **Scenario_20**: Test AI review generation and submission functionality.

Fixtures:
- `chrome_driver_setup`: Provides a configured Chrome WebDriver for browser automation.
- `logger_setup`: Provides a logger instance for logging test execution details.

Preconditions:
- The CarSphere application must be running and accessible at the predefined URL.
- Chrome WebDriver must be installed and configured for Selenium.
- User accounts (e.g., admin and regular users) must exist in the system.
- AI review generation service must be functional for Scenario 20.

Usage:
Run the tests using pytest:
```bash
    pytest test_gallery.py
"""
import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestGUIAndRedirections:
    """
    Test Class: TestGUIAndRedirections

    This class groups all GUI-related tests and redirection validations for the CarSphere application.
    It focuses on verifying the correct appearance, behavior, and functionality of graphical elements on the Cars gallery page,
    ensuring a consistent user experience and proper navigation behavior.

    Key Objectives:
    1. Validate the main page background image to ensure it matches the expected design.
    2. Test branding icon functionality, ensuring it redirects correctly to the application's Home Page.
    3. Verify the LinkedIn icon redirection, confirming it navigates to the correct LinkedIn profile.

    Test Scenarios:
    - **Scenario_16**: Verify that the main page background image is displayed correctly.
    - **Scenario_17**: Validate that the CarSphere branding icon redirects to the Home Page.
    - **Scenario_18**: Confirm that the LinkedIn icon redirects to the 'Israel-Wasserman' LinkedIn profile.

    Fixtures:
    - `chrome_driver_setup`: Provides a Selenium Chrome WebDriver instance for browser automation.
    - `logger_setup`: Provides a logger instance for recording detailed test execution steps and results.

    Preconditions:
    - The CarSphere application must be running and accessible at the predefined URL.
    - Chrome WebDriver must be installed and configured for Selenium.
    - Proper internet access to validate external links (e.g., LinkedIn).

    Execution:
    Run the tests using pytest with the following markers:
    - **smoke**: For quick checks on GUI appearance (Scenario 16).
    - **system** and **functional**: For redirection and link functionality validation (Scenarios 17 and 18).
    """

    """Scenario_16"""
    @pytest.mark.smoke
    @pytest.mark.gui
    def test_016_main_page_background(self, chrome_driver_setup, logger_setup):
        """
        Test Scenario: test_016_main_page_background

        Test Description:
        This test verifies that the main website background image is displayed correctly on the CarSphere homepage.
        The test navigates to the homepage, retrieves the `background-image` CSS property, and compares it with the expected image URL.

        Test Steps:
        1. Open the CarSphere homepage in a Chrome browser.
        2. Maximize the browser window to ensure full visibility.
        3. Retrieve the CSS `background-image` property of the `<body>` element.
        4. Compare the retrieved background image URL to the expected URL.

        Assertions:
        - The background image URL matches the predefined expected URL.

        Preconditions:
        - The CarSphere application must be running and accessible at the predefined URL.
        - Chrome browser and WebDriver must be available for test execution.

        Parameters:
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance.
        :param logger_setup: Fixture that provides a logger instance for recording test execution logs.

        Test Results:
        - On Success: Logs indicate that the background image matches the expected URL, and the test passes.
        - On Failure: Logs the discrepancy in the background image and raises an `AssertionError`.

        :return: None. The test performs assertions and logs results.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_16 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home page'")
        driver.maximize_window()
        logger.info("maximizing window")
        background_image_url = 'url("https://carsphere.onrender.com/static/background_image/background_showroom.jpg")'
        background_image = driver.find_element(By.TAG_NAME, "body").value_of_css_property("background-image")
        # Validate application background image
        logger.info("Validate application background image")
        try:
            assert background_image == background_image_url, (f"wrong background img,"
                                                              f" got {background_image}, expected {background_image_url}"
                                                              f"\nScenario_16 Failed")
        except AssertionError as message:
            logger.error(message)
            raise AssertionError(message)
        else:
            logger.info("Scenario_16 = passed")

        driver.close()
        print("Scenario_16 Finished")

    """Scenario_17"""
    @pytest.mark.system
    @pytest.mark.functional
    def test_017_branding_link(self, chrome_driver_setup, logger_setup):
        """
        Test Scenario: test_017_branding_link

        Test Description:
        This test verifies that the CarSphere branding image displays the correct source URL and ensures its functionality
        by validating that the branding icon links to the expected image location.

        Test Steps:
        1. Open the CarSphere homepage in a Chrome browser.
        2. Locate the branding icon element using its class name.
        3. Retrieve the `src` attribute (URL) of the branding icon.
        4. Compare the retrieved URL to the predefined expected branding image URL.

        Assertions:
        - The branding icon's source URL matches the expected image URL.

        Preconditions:
        - The CarSphere application must be running and accessible at the predefined URL.
        - Chrome browser and WebDriver must be available for test execution.

        Parameters:
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for logging the test execution steps and results.

        Test Results:
        - On Success: Logs confirm that the branding icon's source matches the expected URL, and the test passes.
        - On Failure: Logs the discrepancy in the branding icon URL and raises an `AssertionError`.

        :return: None. The test validates the branding link and logs the outcome.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrom web driver' setup success")
        print("Scenario 17 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        branding_element = driver.find_element(By.CLASS_NAME, "branding-icon")
        current_branding_icon_url = branding_element.get_attribute("src")
        expected_branding_url = "https://carsphere.onrender.com/static/background_image/branding.png"
        # Validate the CarSphere branding icon redirection URL (shall be redirected to Home Page)
        logger.info("Validate the CarSphere branding icon redirection URL (shall be redirected to Home Page)")
        try:
            assert current_branding_icon_url == expected_branding_url
            logger.info("Scenario 17 Passed")
        except AssertionError as e:
            logger.error(f"Expected {expected_branding_url}, got {current_branding_icon_url}")
            logger.error(f"Scenario_17 Failed")
            raise AssertionError(e)

        driver.close()
        print("Scenario_17 Finished")

    """Scenario_18"""
    @pytest.mark.system
    @pytest.mark.functional
    def test_018_linkedin_icon_link(self, chrome_driver_setup, logger_setup):
        """
        Test Scenario: test_018_linkedin_icon_link

        Test Description:
        This test verifies that the LinkedIn icon on the CarSphere homepage redirects to the correct LinkedIn profile
        ("Israel-Wasserman" profile). The test ensures that the LinkedIn icon link functions properly.

        Test Steps:
        1. Open the CarSphere homepage in a Chrome browser.
        2. Locate the LinkedIn icon element using its XPath.
        3. Click the LinkedIn icon to open the redirection URL in a new browser tab.
        4. Switch to the new browser tab and retrieve the current URL.
        5. Verify that the URL contains the expected profile identifier: "israel-wasserman".

        Assertions:
        - The current URL in the new tab contains the expected LinkedIn profile identifier.

        Preconditions:
        - The CarSphere application must be running and accessible at the predefined URL.
        - Chrome browser and WebDriver must be available for test execution.
        - The LinkedIn profile link must be active and functional.

        Parameters:
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for logging test execution details.

        Test Results:
        - On Success: Logs confirm that the LinkedIn icon redirects to the expected LinkedIn profile, and the test passes.
        - On Failure: Logs the discrepancy in the URL and raises an `AssertionError`.

        :return: None. The test validates LinkedIn icon functionality and logs the outcome.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario 18 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//p/a/img[@class='linkedin-icon']").click()
        my_windows = driver.window_handles
        driver.switch_to.window(my_windows[1])
        expected_linkedin_url_content = "israel-wasserman"
        current_linkedin_url = driver.current_url
        # Validate that the LinkedIn icon redirection URL redirects to 'Israel Wasserman' LinkedIn profile
        logger.info("Validate that the LinkedIn icon redirection URL redirects to 'Israel Wasserman' LinkedIn profile")
        try:
            assert expected_linkedin_url_content in current_linkedin_url
            logger.info("Scenario 18 Passed")
        except AssertionError:
            logger.error(f"Expected that the {expected_linkedin_url_content} will be part of the link, "
                         f"got {current_linkedin_url}")
            logger.info("Scenario_18 Failed")
            raise

        driver.close()
        print("Scenario_18 Finished")

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestReviews:
    """This class groups the users review testing (Manual review and AI review)"""

    """Scenario_19"""
    @pytest.mark.sanity
    @pytest.mark.functional
    def test_019_user_manual_review(self, chrome_driver_setup, logger_setup):
        """
        Test Scenario: test_019_user_manual_review

        Test Description:
        This test verifies that a user can successfully submit a manual review for a car and ensures the review appears in the
        'Users Review' section of the CarSphere application.

        Test Steps:
        1. Open the CarSphere homepage in a Chrome browser.
        2. Log in to the application using valid user credentials.
        3. Navigate to the car catalog and select the last car in the list.
        4. Submit a manual review with randomly generated text.
        5. Verify that a success message is displayed confirming the review submission.
        6. Ensure the newly submitted review appears in the 'Users Review' section.

        Assertions:
        1. The success message confirms that the review was successfully added.
        2. The review text appears correctly in the 'Users Review' area, matching the submitted content.

        Preconditions:
        - The CarSphere application must be running and accessible at the predefined URL.
        - Chrome browser and WebDriver must be available for test execution.
        - A user account with valid credentials (e.g., `user3`) must exist in the system.

        Parameters:
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for logging test execution details.

        Test Results:
        - On Success: Logs confirm that the review was successfully submitted and appears in the 'Users Review' area.
        - On Failure: Logs detail the failure in review submission or visibility and raise an `AssertionError`.

        :return: None. The test validates manual review functionality and logs the outcome.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrom web driver' setup success")
        print("Scenario_19 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application Home Page")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        cars_element_list = driver.find_elements(By.XPATH, "//div/div/div/a")
        cars_element_list[-1].click()
        manual_review_to_be_added = "Auto Manual Review" + ''.join(random.choices(string.digits, k=3))
        driver.find_element(By.XPATH, "//form/textarea").send_keys(manual_review_to_be_added)
        driver.find_element(By.ID, "submit").click()
        add_review_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        # Assertion_1: Validate that review successfully submitted
        logger.info("Assertion_1: Validate that review successfully submitted")
        assert add_review_success_message.text == "Review added successfully!", \
            "Review do not added. Expected - review shall be added\nFirst part of Scenario_19 Failed"
        logger.info("Review added successfully")
        logger.info("First part of Scenario_19 Passed...")

        # Assertion_2: Validate that review appears in the 'Users Review' area
        logger.info("Assertion_2: Validate that review appears in the 'Users Review' area")
        users_review_list = driver.find_elements(By.XPATH, "//ul/li")
        assert users_review_list[-1].text == f"user3: {manual_review_to_be_added}", \
            "Review do not appears in the 'Users Review' area\nSecond part of Scenario_19 Failed"
        logger.info("Review appears in the 'Users Review' area")
        logger.info("Scenario_19 Passed")

        driver.close()
        print("Scenario_19 Finished")

    """Scenario_20"""
    @pytest.mark.integration
    @pytest.mark.functional
    def test_020_user_ai_review(self, chrome_driver_setup, logger_setup):
        """
        Test Scenario: test_020_user_ai_review

        Test Description:
        This test verifies that a user can generate and submit a review using the AI review generation option
        in the CarSphere application. It ensures that the AI-generated review is successfully created and added to the system.

        Test Steps:
        1. Open the CarSphere homepage in a Chrome browser.
        2. Log in to the application using valid user credentials.
        3. Navigate to the car catalog and select the last car in the list.
        4. Click on the "AI Review" button to trigger the AI review generation process.
        5. Wait for the AI-generated review to populate the input field.
        6. Submit the generated review.
        7. Verify the success message confirming that the review was successfully added.

        Assertions:
        1. Validate that the AI review input field is populated with generated content (non-empty).
        2. Confirm that the success message indicates the review was successfully submitted.

        Preconditions:
        - The CarSphere application must be running and accessible at the predefined URL.
        - Chrome browser and WebDriver must be available for test execution.
        - A user account with valid credentials (e.g., `user3`) must exist in the system.
        - The AI review generation service must be functional and return a response within the timeout window.

        Parameters:
        :param chrome_driver_setup: Fixture that provides a configured Chrome WebDriver instance for browser automation.
        :param logger_setup: Fixture that provides a logger instance for logging test execution steps and results.

        Test Results:
        - On Success:
          - The AI-generated review is displayed in the input field.
          - The review submission success message is displayed, confirming successful addition of the review.
        - On Failure:
          - Logs detail issues with AI review generation or submission, and the test raises an `AssertionError`.

        :return: None. The test validates AI-generated review functionality and logs the outcome.
        """
        logger = logger_setup
        logger.debug("'Logger' setup success")
        driver = chrome_driver_setup
        logger.debug("'Chrome web driver' setup success")
        print("Scenario_20 Begin")
        driver.get("https://carsphere.onrender.com/")
        logger.info("Redirecting to application 'Home Page'")
        driver.find_element(By.XPATH, "//nav/a[@href='/login']").click()
        driver.find_element(By.XPATH, "//div/input[@id='username']").send_keys("user3")
        driver.find_element(By.XPATH, "//div/input[@id='password']").send_keys("user3")
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()
        cars_element_list = driver.find_elements(By.XPATH, "//div/div/div/a")
        cars_element_list[-1].click()
        driver.find_element(By.ID, "ai-review-button").click()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda _driver: driver.find_element(By.ID, "review-input").get_attribute("value") != '')
        ai_review_input = driver.find_element(By.ID, "review-input").get_attribute("value")
        logger.info(f"Generated AI review returned from external service: {ai_review_input}")
        # Assertion_1: Validate that AI review (from external API) generated successfully
        logger.info("Assertion_1: Validate that AI review (from external API) generated successfully")
        assert ai_review_input != '', "AI review failed to be generated\nFirst part of Scenario_20 Failed"
        logger.info("AI review successfully generated")
        logger.info("First part of Scenario_20 passed...")

        # Assertion_2: Validate that AI review successfully submitted
        logger.info("Assertion_2: Validate that AI review successfully submitted")
        driver.find_element(By.ID, "submit").click()
        add_ai_review_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
        assert add_ai_review_success_message.text == "Review added successfully!", \
            "Review do not added. Expected - review shall be added\n Second part of Scenario_20 Failed"
        logger.info("Review added successfully")
        logger.info("Second part of Scenario_20 Passed")

        driver.close()
        print("Scenario_20 Finished")