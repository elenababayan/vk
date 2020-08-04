
from .locators import LoginPageLocators
from .base_page import BasePage

class LoginForm(BasePage):

    def go_to_enter_login(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.get("89094163112")

    def go_to_enter_password(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.get("Vfvjxrf908+")

    def puss_the_button(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()

