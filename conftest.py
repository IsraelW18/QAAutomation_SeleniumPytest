from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging

@pytest.fixture
def chrome_driver_setup():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@pytest.fixture
def logger_setup():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('test_third.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger