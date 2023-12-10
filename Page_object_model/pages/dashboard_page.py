from pages.base_page import BasePage
from utils.locators import DashboardPageLocators


class DashboardPage(BasePage):

    def myInfo(self):
        self.click_element(*DashboardPageLocators.MyInfo)

    def verify_myInfo_page_open(self, expected_url):
        # verify login or not
        actual_url = self.driver.current_url

        if actual_url == expected_url:
            print(f"My Info open successfully.")
        else:
            print(f"My Info open Unsuccessful.")
