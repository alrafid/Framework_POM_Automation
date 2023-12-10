from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")


class RegistrationPageLocators:
    FIRST_NAME = (By.NAME, 'name')


class DashboardPageLocators:
    MyInfo = (By.LINK_TEXT, 'My Info')


