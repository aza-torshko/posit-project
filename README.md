# Posit.Cloud Playwright Automation

##  Setup Instructions

### Make Sure You Have the Following Installed:
-  **Python 3.x** (Check with `python --version` or `python3 --version`)
-  **Pipenv** (Install with `pip install pipenv`)
-  **Playwright** (Install with `pipenv run playwright install`)

### 1 Clone the Repository
```bash
git clone https://github.com/yourusername/posit-cloud-automation.git
```

### 2 Install Dependencies
```bash
pip install pipenv  # Install pipenv if not installed
pipenv install  # Install project dependencies
pipenv run playwright install  # Install Playwright browsers
```

### 3 Run Tests

####  Run All Tests
```bash
pipenv run pytest
```

####  Run a Specific Test
```bash
pipenv run pytest tests/test_create_space_project.py
```

####  Run a Specific Test Case
```bash
pipenv run pytest -k test_create_space_and_project
```

####  Run Tests in Headless Mode
```bash
pipenv run pytest --headless
```

####  Generate an HTML Report
```bash
pipenv run pytest --html=report.html --self-contained-html
```

##  Why These Tools?

###  Python
Python is a widely used programming language in test automation.

###  Playwright
Playwright is automation framework that supports multiple browsers (Chromium, Firefox, WebKit) and enables fast, reliable end-to-end testing.

###  Pytest
Pytest is a testing framework for Python that makes writing tests simple and readable.

###  Pipenv
Pipenv helps manage dependencies and virtual environments.

## 📌 Folder Structure
```bash
📂 posit-project/
│-- 📂 tests/
│   ├── test_create_space_project.py  # Tests space/project creation
│-- 📂 pages/
│   ├── login_page.py  # Page locators
│-- 📂 actions/
│   ├── login_actions.py  # Business logic
│-- 📂 config/
│   ├── credentials.py  # Username and Password
│-- 📄 conftest.py  # Fixtures
│-- 📄 Pipfile  # Dependencies
│-- 📄 README.md  # Documentation
```

## 🛠 Troubleshooting
#### 🔹 Pipenv Not Found?
```bash
python3 -m pip install --user pipenv
```

#### 🔹 Playwright Not Installed?
```bash
pipenv run playwright install
```

#### 🔹 Browser Not Launching?
```bash
pipenv run playwright install
pipenv run pytest --headed
```

### ✅ Now You're Ready to Automate Posit.Cloud!