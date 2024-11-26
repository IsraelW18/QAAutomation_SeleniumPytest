"""This module includes testing for CarSphere gallery"""
import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestGUIAndRedirections:
    """This class groups the Cars gallery GUI testing"""

    """Scenario_16"""
    @pytest.mark.smoke
    @pytest.mark.gui
    def test_016_main_page_background(self, chrome_driver_setup, logger_setup):
        """
        Test Description: Testing the main website background image.
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
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
        Test Description: Testing the CarSphere branding image URL (redirection to Home)
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
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
        Test Description: Testing the LinkedIn icon URL (redirection to "Israel-Wasserman" LinkedIn profile)
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
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
        Test Description: Testing user manual review
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
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
        Test Description: Testing adding a review using the AI option review generation
        :param chrome_driver_setup:
        :param logger_setup:
        :return:
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