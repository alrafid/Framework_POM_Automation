import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import LOGIN_URL, BROWSER_NAME

# Define test data as list of tuples (username, password)
test_data = [
    ("Admin", "admin123")
]


@pytest.fixture
def setup():
    if BROWSER_NAME == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif BROWSER_NAME == 'firefox':
        driver = webdriver.Firefox()
    elif BROWSER_NAME == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser:", BROWSER_NAME)

    driver.get(LOGIN_URL)

    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password", test_data)
def test_dashboard(setup, username, password):
    login_page = LoginPage(setup)
    login_page.verify_login_page_open()
    login_page.login(username, password)
    # add some verification: verify login using expected url
    login_page.verify_login("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    dashboard_page = DashboardPage(setup)
    dashboard_page.myInfo()
    dashboard_page.verify_myInfo_page_open(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
