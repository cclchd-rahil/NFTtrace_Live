# NFTtrace Live Application Testing

This repository contains automated test scripts and setup documentation for testing the NFTtrace Live Application. The testing suite is designed to verify the application's functionality and reliability through automated tests using Selenium, Pytest, and Jenkins CI/CD.

# Table of Contents
* Project Overview
* Prerequisites
* Running Tests
* Continuous Integration (CI) Pipeline

# Project Overview

The NFTtrace Live Application allows users to manage NFT certificates and their respective details. This testing repository automates the testing process for the application's login functionality, and ensures that new updates do not break existing functionality.

# Key Features:

* Automated testing for login functionalities.
* Continuous Integration (CI) pipeline that automates the testing process on each code push.
* Scheduled builds at 9 am, 12 pm, 3 pm, and 6 pm daily.

# Prerequisites

To set up and run the tests, ensure you have the following installed:

* Python 3.8 or higher
* Selenium WebDriver
* Pytest
* Jenkins (for CI/CD pipeline setup)
* Git

# Running Tests
To run all tests:

    pytest


To run a specific test case, specify the test file or test name:

    pytest tests/test_login.py

To generate report for run tests:

    pytest --html=report.html
    


# Continuous Integration (CI) Pipeline

The Jenkins CI/CD Pipeline is set up to automate testing with the following structure:

* Trigger: The pipeline is triggered on every code push to the GitHub repository.
* Scheduled Builds: Runs automatically at 9 am, 12 pm, 3 pm, and 6 pm daily.
Stages:
    * Build: Pulls the latest code and sets up dependencies.
    * Test Execution: Runs all automated test cases, including login and UI tests.
    * Reporting: Displays pass/fail results and test coverage in Jenkins.
 

