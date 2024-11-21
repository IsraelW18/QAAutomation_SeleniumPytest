"""
Scenario_1.
Test description: Main website background image.
"""

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://carsphere.onrender.com/")
driver.maximize_window()
background_image_url = 'url("https://carsphere.onrender.com/static/background_image/background_showroom.jpg")'
background_image = driver.find_element(By.TAG_NAME, "body").value_of_css_property("background-image")
assert background_image == background_image_url, f"background_image mismatch  got {background_image}, expected {background_image_url}"
print("Scenario_1 = Passed: Background image is as expected")
# driver.quit()

"""
Scenario_2.
Test Description: Navigate to home page using "Home' button.
"""
# driver = create_driver()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
driver.get("https://carsphere.onrender.com/")
home_page_url = driver.current_url
driver.get("https://carsphere.onrender.com/login")
login_page = driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Login')]")
login_page.click()
home_page = driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Home')]")
home_page.click()
assert driver.current_url == home_page_url, f"Nav' to {home_page_url} using 'Home' button not success"
print(f"Scenario_2 = Passed: Navigation to Home page '{home_page_url}' success")
# driver.quit()
"""
Scenario_3.
Test description: Navigate to 'Login' page
"""
# driver = create_driver()
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
driver.get("https://carsphere.onrender.com/")
login_page_url = 'https://carsphere.onrender.com/login'
driver.find_element(By.XPATH, "//nav/a[contains(text(), 'Login')]").click()
current_url = driver.current_url
assert current_url == login_page_url, f"Failed: expected '{login_page_url}', got '{current_url}'"
print(f"Scenario_3 = Passed: Navigation to Login page '{login_page_url}' success")

"""
Scenario_4.
Test Description: Linkedin link validation (both: 'Linkedin' icon & 'Israel Wasserman ©')
"""
driver.get("https://carsphere.onrender.com/")
# Collecting the LinkedIn icon link redirection url to 'current_url_1' variable
driver.find_element(By.CLASS_NAME, "linkedin-icon").click()
my_windows = driver.window_handles
driver.switch_to.window(my_windows[1])
current_url_1 = driver.current_url
# Collecting the LinkedIn link of "Israel Wasserman ©" href redirection url to 'current_url_2' variable
driver.switch_to.window(my_windows[0])
driver.find_element(By.XPATH, "//p/a[@target='_blank']").click()
driver.switch_to.window(my_windows[1])
current_url_2 = driver.current_url
# Assertion related to the URL redirected from LinkedIn icon
assert ("linkedin.com" in current_url_1 and "israel-wasserman"
        in current_url_1), f"expected redirect to Israel W Linkedin profile, got {current_url_1}"
print("Scenario_4.1 = Passed: Navigation to 'Israel Wasserman' linkedin profile via LinkedIn icon success")
# Assertion related to the URL redirected from "Israel Wasserman ©" href link
assert ("linkedin.com" in current_url_2 and "israel-wasserman"
        in current_url_2), f"expected redirect to Israel W Linkedin profile, got {current_url_2}"
print("Scenario_4.2 = Passed: Navigation to 'Israel Wasserman' linkedin profile via 'Israel Wasserman ©' href success")

"""
Scenario_5:
"""

# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']"))).click()

