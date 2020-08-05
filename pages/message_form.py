from .base_page import BasePage
from .locators import MessageLocators


class MessageForm(BasePage):

    def go_to_the_message(self):
        letter = self.browser.find_element(*MessageLocators.MESSAGE)
        letter.click()

