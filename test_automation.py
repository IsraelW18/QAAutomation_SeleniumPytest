"""
Project_3:
Selenium automaton testing for the application developed as "Project_2 (Flask)" - "CarSphere" application.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.usefixtures("chrome_driver_setup", "logger_setup")
class TestGUIAndRedirections:
    """
    Scenario_1.
    Description: Testing the main website background image.
    """
    @pytest.mark.gui
    def test_main_page_background(self, chrome_driver_setup, logger_setup):
        logger = logger_setup
        logger.info("logger setup successfully")
        driver = chrome_driver_setup
        logger.info("web driver setup successfully")
        driver.get("https://carsphere.onrender.com/")
        logger.info("GET http request for the main page")
        driver.maximize_window()
        logger.info("maximizing window")
        background_image_url = 'url("https://carsphere.onrender.com/static/background_image/background_showroom.jpg")'
        background_image = driver.find_element(By.TAG_NAME, "body").value_of_css_property("background-image")
        try:
            assert background_image == background_image_url, f"wrong background img, got {background_image}, expected {background_image_url}"
        except AssertionError as message:
            logger.error(message)
            raise AssertionError(message)
        else:
            logger.info("Scenario_1 = passed")
        driver.close()

    """
    Scenario_2.
    Description: Testing the amount of cars catalog images.
    """
    @pytest.mark.gui
    def test_cars_catalog_item_count(self, chrome_driver_setup, logger_setup):
        logger = logger_setup
        logger.info("logger setup successfully")
        driver = chrome_driver_setup
        logger.info("web driver setup successfully")
        driver.get("https://carsphere.onrender.com/")
        logger.info("GET http request for the main page")
        cars_catalog_items = driver.find_elements(By.CLASS_NAME, "car-item")
        try:
            # Checking the amount of the 'cars-item' currently exist in the Catalog
            assert len(cars_catalog_items) == 6, f"Catalog shall include 6 items, got {len(cars_catalog_items)}"
        except AssertionError as message:
            logger.error(message)
            raise AssertionError(message)
        else:
            logger.info("Scenario_2 = passed")
        driver.close()

    """
    Scenario_3.
    Description: Validate the cars catalog images url.
    """
    @pytest.mark.gui
    def test_cars_catalog_items_images(self, chrome_driver_setup, logger_setup):
        driver = chrome_driver_setup
        logger = logger_setup
        driver.get("https://carsphere.onrender.com/")
        car_images = ['https://carsphere.onrender.com/static/images/1_ToyotaCorolla.jpg',
                      'https://carsphere.onrender.com/static/images/3_Porsche.jpg',
                      'https://carsphere.onrender.com/static/images/6_Mercedes_BenzSClass.jpg',
                      'https://carsphere.onrender.com/static/images/9_Jeep_Wrangler.jpg',
                      'https://carsphere.onrender.com/static/images/8_Ford_Transit.jpg',
                      'https://carsphere.onrender.com/static/images/7_BMW_7Series.jpg']
        cars_catalog_items = driver.find_elements(By.CLASS_NAME, "car-item")

        test_passed = []
        for car_item in cars_catalog_items:

            image = car_item.find_element(By.TAG_NAME, "img").get_attribute("src")
            expected_image = car_images[cars_catalog_items.index(car_item)]
            try:
                assert image == expected_image
            except AssertionError as e:
                logger.error(f"got {image} which is incorrect, expected {expected_image}")
                test_passed.append(False)
                raise AssertionError(e)
            else:
                test_passed.append(True)
            finally:
                continue

        if not test_passed:
            print("Scenario 3 = no images found")
            assert False, "No images found"
        if all(test_passed):
            print("Scenario 3 = passed")
        else:
            print("Scenario 3 = failed")
            assert False, f"One or more images did not match the expected result"
        driver.close()

    """
    Scenario_4.
    Test Description: Testing the branding URL (redirection to Home)
    """
    @pytest.mark.gui
    def test_branding_link(self, chrome_driver_setup, logger_setup):
        driver = chrome_driver_setup
        logger = logger_setup
        logger.info("Scenario 4 begin")
        driver.get("https://carsphere.onrender.com/")
        branding_element = driver.find_element(By.CLASS_NAME, "branding-icon")
        current_branding_icon_url = branding_element.get_attribute("src")
        expected_branding_url = "https://carsphere.onrender.com/static/background_image/branding.png"
        try:
            assert current_branding_icon_url == expected_branding_url
            logger.info("Scenario 4 = passed")
        except AssertionError as e:
            logger.error(f"Expected {expected_branding_url}, got {current_branding_icon_url}")
            raise AssertionError(e)
        driver.close()

    """
    Scenario_5.
    Test Description: Linkedin icon url validation
    """

    def test_linkedin_icon_link(self, chrome_driver_setup, logger_setup):
        driver = chrome_driver_setup
        logger = logger_setup
        logger.info("Scenario 5 begin")
        driver.get("https://carsphere.onrender.com/")
        driver.find_element(By.XPATH, "//p/a/img[@class='linkedin-icon']").click()
        my_windows = driver.window_handles
        driver.switch_to.window(my_windows[1])
        expected_linkedin_url_content = "israel-wasserman"
        current_linkedin_url = driver.current_url
        try:
            assert expected_linkedin_url_content in current_linkedin_url
            logger.info("Scenario 5 = passed")
        except AssertionError:
            logger.error(f"Expected that the {expected_linkedin_url_content} will be part of the link, "
                         f"got {current_linkedin_url}")
            raise
        driver.close()

    """
    Scenario_6.
    Test Description: Linkedin url validation of 'Israel Wasserman ©' element 
    """
    def test_israel_wasserman_element_linkedin_url(self, chrome_driver_setup, logger_setup):
        driver = chrome_driver_setup
        logger = logger_setup
        logger.info("Scenario 6 begin")
        driver.get("https://carsphere.onrender.com/")
        driver.find_element(By.XPATH, "//p/a[contains(text(), 'Israel Wasserman ©')]").click()
        my_windows = driver.window_handles
        driver.switch_to.window(my_windows[1])
        expected_linkedin_url_content = "israel-wasserman"
        current_linkedin_url = driver.current_url
        try:
            assert expected_linkedin_url_content in current_linkedin_url
            logger.info("Scenario 6 = passed")
        except AssertionError:
            logger.error(f"Expected that the {expected_linkedin_url_content} will be part of the link, "
                         f"got {current_linkedin_url}")
            raise
        driver.close()


