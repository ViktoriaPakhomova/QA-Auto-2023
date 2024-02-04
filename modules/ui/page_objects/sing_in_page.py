from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SingInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SingInPage.URL)

    def try_login(self, username, password):
        # Find the field in which we will enter the wrong username or email address
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter an incorrect username or email address
        login_elem.send_keys(username)

        # Find the field in which we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter the wrong password
        pass_elem.send_keys(password)

        # Find the buttom sing in
        btm_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate a left mouse click
        btm_elem.click

    def check_title(self, expected_title):
        return self.driver.title == expected_title