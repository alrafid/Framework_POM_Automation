from pages.base_page import BasePage
from utils.locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.input_text(*LoginPageLocators.USERNAME_INPUT, username)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)

    def verify_login_page_open(self):
        # Verify Login open successfully
        expected_title = "OrangeHRM"
        actual_title = self.driver.title

        if actual_title == expected_title:
            print(f"Orange Login page open successfully.Title is: {actual_title}")
        else:
            print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

    def verify_login(self, expected_url):
        # verify login or not
        actual_url = self.driver.current_url

        if actual_url == expected_url:
            print(f"Login successfully.")
        else:
            print(f"Login Unsuccessful.")

        print("Test Case Executed Successfully.......")
