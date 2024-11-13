import time
import pytest
from pages.login_page import LoginPage
from utils.config import driver

@pytest.mark.login
def test_valid_login(driver):
    """Verify successfull login."""
    login_page =LoginPage(driver)

    driver.get("https://app.nfttrace.com/login")
    driver.maximize_window()
    login_page.enter_email("superadmin@chaincodeconsulting.com")
    login_page.enter_password("admin@123")
    login_page.click_login()

    expected_title = "NFTtrace - Login to Manage and Track Your NFTs with Ease"
    assert driver.title == expected_title, f"Expected title '{expected_title}', but got '{driver.title}'"



