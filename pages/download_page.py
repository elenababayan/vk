from .base_page import BasePage
import requests
from .locators import DownloadLocators, LoginPageLocators, MessageLocators, DialogueLocators


class DownloadPage(BasePage):

    def go_to_enter_login(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys('89094163112')

    def go_to_enter_password(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('Vfvjxrf908+')

    def push_the_button(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()

    def go_to_the_message(self):
        letter = self.browser.find_element(*MessageLocators.MESSAGE)
        letter.click()

    def go_to_the_page_dialogue(self):
        dialogue = self.browser.find_element(*DialogueLocators.DIALOGUUE)
        dialogue.click()

    def go_to_the_download(self, img=None):
        download = self.browser.find_element(*DownloadLocators.DOWNLOAD)
        download.click()
        download_two = self.browser.find_element(*DownloadLocators.DOWNLOAD_TWO)
        download_two.click()
        p = requests.get(img)
        out = open("/Users/bulbik/vk", "wb")
        out.write(p.content)
        out.close()


