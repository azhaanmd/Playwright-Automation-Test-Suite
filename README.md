# 📘 Playwright Automation Test Suite

An end-to-end automation framework integrating UI, API, and Database testing using Playwright, Pytest, and Docker.  
This suite supports parallel test execution, generates comprehensive HTML and JSON reports, and integrates seamlessly with GitHub Actions for continuous integration.

---

## 🚀 Features

- ✅ **UI Testing**: Automated browser interactions using Playwright.
- ✅ **API Testing**: Validation of RESTful APIs with dynamic data handling.
- ✅ **Database Testing**: Integration with PostgreSQL (Neon) for backend verification.
- ✅ **Parallel Execution**: Powered by `pytest-xdist`.
- ✅ **Reporting**: Generates detailed HTML and JSON reports.
- ✅ **Dockerized**: Fully containerized environment for consistent execution.
- ✅ **CI/CD**: GitHub Actions workflow for automatic test runs on each commit.

---

## 🛠️ Tech Stack

| Category       | Technology       |
|----------------|------------------|
| Language       | Python 3.11      |
| Framework      | Pytest           |
| Automation     | Playwright       |
| CI/CD          | GitHub Actions   |
| Containerization | Docker         |
| Database       | PostgreSQL (Neon) |

---

## 📂 Project Structure
Playwright-Automation-Test-Suite/
├── .github/workflows/ # GitHub Actions workflows
│ └── ci.yml # GitHub Actions CI workflow file
├── assets/ # Screenshots or static assets
├── fixtures/ # Pytest fixtures
├── logs/ # Log files from test runs
├── pages/ # Page Object Model classes
├── report/ # HTML & JSON test reports
├── test_data/ # Test data in JSON
├── tests/ # Test cases
│ ├── api/ # API tests
│ ├── db/ # DB tests
│ └── ui/ # UI tests
├── utils/ # Helper functions
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── run_test_suite.bat
└── pytest.ini # Pytest config

## ▶️ Run Tests
pytest tests/ -v -n auto --html=report/report.html --self-contained-html --capture=tee-sys

## 🐳 Docker Support
🏗️ Build Docker Image
docker build -t playwright-tests .
🧪 Run Inside Container
docker run --rm playwright-tests

## 🔄 CI/CD with GitHub Actions
This project automatically runs all test suites on push using GitHub Actions.
Workflow file: .github/workflows/ci.yml

No extra setup needed. Simply push code to trigger the pipeline.

## 📊 Reports
After test execution:

✅ HTML Report: report/report.html

✅ JSON Report: report/report.json

Open the HTML report in any browser for detailed insights.


## 🙌 Contributing
Feel free to fork this repo, create a branch, and open a pull request with your improvements!

## 📬 Contact
For feedback or questions, reach out to: 
- https://github.com/azhaanmd/
- azhaan0810@gmail.com

⭐ If you found this useful, don't forget to star the repo!

