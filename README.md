# QA Automation Portfolio Project

### Overview
This repository serves as a portfolio project showcasing my skills in QA automation and Python development. It demonstrates the development and execution of automated tests using Python, Selenium, and Pytest. The project includes comprehensive UI tests, API tests, as well as validations for both server-side and client-side functionality. These tests are designed to run on a custom web application I developed, [Car Sphere (Live)](https://carsphere.onrender.com/), using Python and Flask, leveraging SQLite and SQLAlchemy for database management.

The source code for the project is available in my [CarSphere Repository](https://github.com/IsraelW18/CarSphere.git).

The automated testing suite ensures the reliability, scalability, and robustness of the application by covering multiple layers:
- UI Tests: Validate the functionality and behavior of the web interface.
- API Tests: Ensure that API endpoints work as expected and return the correct responses.
- Server-Side Tests: Verify the backend logic and database interactions.
- Client-Side Tests: Check client-side behavior, such as JavaScript validations and DOM manipulations.
- The project highlights not only my ability to create comprehensive and efficient automation frameworks but also my proficiency in developing scalable web applications using Python and Flask, adhering to best practices in software testing and development.

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
```bash
Automation/
├── .venv/                 # Virtual environment
├── assets/                # Assets directory (currently empty)
├── test_images/           # Test images for automation
│   ├── AutoTestCar.jpg
│   ├── AutoTestCar_bak.jpg
│   └── AutoTestCar_bak_2.jpg
├── conftest.py            # Shared fixtures and setup
├── README.md              # Project description
├── report.html            # Test execution report
├── test_admin.py          # Tests for admin-related functionality
├── test_auth.py           # Tests for authentication functionality
├── test_gallery.py        # Tests for gallery-related functionality
├── test_third.log         # Log file for third test execution
└── users.txt              # File containing user data for testing
```

### Setup Instructions

#### Prerequisites
- Make sure you have Python 3.12.6 installed on your system.
- Install pip (Python's package manager) if it is not already installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IsraelW18/QAAutomation_SeleniumPytest.git

2. **Navigate to the project directory**:
   ```bash
   git clone https://github.com/IsraelW18/QAAutomation_SeleniumPytest.git
   
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the test**:
   ```bash
   pytest

### How to Run Tests
*  **Run all test**:
   ```bash
   pytest

*  **Run a specific test file**:
   ```bash
   pytest tests/<test_example.py>

*  **Generate detailed test reports**:
   ```bash
   pytest --html=report.html --self-contained-html

## Contact
For any questions or feedback, feel free to reach out via [GitHub](https://github.com/IsraelW18) or [LinkedIn](https://www.linkedin.com/in/israel-wasserman/).