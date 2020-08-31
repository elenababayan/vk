from .locators import MessageLocators
from .base_page import BasePage
from .locators import DialogueLocators
from .locators import DispatchLocators

class LoginForm(BasePage):

    def go_to_the_message(self):
        letter = self.browser.find_element(*MessageLocators.MESSAGE)
        letter.click()

    def go_to_the_page_dialogue(self):
        dialogue = self.browser.find_element(*DialogueLocators.DIALOGUUE)
        dialogue.click()

    def sending_a_message(self):
        dispatch = self.browser.find_element(*DispatchLocators.DISPATCH)
        dispatch.send_keys(" Hello")
        transfer = self.browser.find_element(*DispatchLocators.TRANSFER)
        transfer.click()


