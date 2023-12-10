import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver
    driver.quit()


def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.verify_login_page_open()
    login_page.login("Admin", "admin123")
    # add some verification: verify login using expected url
    login_page.verify_login("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")


def test_login_invalid(setup):
    login_page = LoginPage(setup)
    login_page.verify_login_page_open()
    login_page.login("Admin123", "admin123")
    # add some verification: verify login using expected url
    login_page.verify_login("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

