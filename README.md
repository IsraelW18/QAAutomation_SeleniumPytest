# QA Automation Portfolio Project

### Overview
This repository serves as a portfolio project showcasing my skills in QA automation. It demonstrates the development and execution of automated UI tests using Python, Selenium, and Pytest. The project highlights my ability to create robust, efficient, and scalable automation frameworks, adhering to best practices in software testing.

### Features
- Automation of end-to-end test cases for web applications.
- Use of Pytest for test organization, parametrization, and reporting.
- Integration of Selenium WebDriver for browser automation.
- Comprehensive test logging and reporting.
- Modular and reusable code structure for easy scalability.

### Technologies Used
- **Python**: Core programming language.
- **Selenium WebDriver**: For browser automation.
- **Pytest**: Framework for organizing and executing tests.
- **Git**: Version control.

### Project Structure

Automation/ ├── .venv/ # Virtual environment ├── assets/ # Assets directory (currently empty) ├── test_images/ # Test images for automation │ ├── AutoTestCar.jpg │ ├── AutoTestCar_bak.jpg │ └── AutoTestCar_bak_2.jpg ├── conftest.py # Shared fixtures and setup ├── README.md # Project description ├── report.html # Test execution report ├── test_admin.py # Tests for admin-related functionality ├── test_auth.py # Tests for authentication functionality ├── test_gallery.py # Tests for gallery-related functionality ├── test_third.log # Log file for third test execution └── users.txt # File containing user data for testing

bash
Copy code

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/IsraelW18/QAAutomation_SeleniumPytest.git
Navigate to the project directory:

bash
Copy code
cd QAAutomation_SeleniumPytest
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the tests:

bash
Copy code
pytest
How to Run Tests
Run all tests:

bash
Copy code
pytest
Run a specific test file:

bash
Copy code
pytest tests/<test_example.py>
Generate detailed test reports:

bash
Copy code
pytest --html=report.html --self-contained-html
Contact
For any questions or feedback, feel free to reach out via GitHub or LinkedIn.