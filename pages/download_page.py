import time

from lib2to3.pgen2 import driver
from .base_page import BasePage
from .locators import DownloadLocators, LoginPageLocators, MessageLocators, DialogueLocators, DispatchLocators

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
        dialogue = self.browser.find_element(*DialogueLocators.DIALOGUUQ)
        dialogue.click()

    def go_to_the_download(self):
        download = self.browser.find_element(*DownloadLocators.DOWNLOAD)
        download.click()
        download_two = self.browser.find_element(*DownloadLocators.DOWNLOAD_TWO)
        download_two.click()
        dispatch = self.browser.find_element_by_xpath("//*[@id='content']/div/div[1]/div[3]/div[2]/div[2]/div[4]/input")
        dispatch.sendFile("C:\\Users\\DsXac\\vk\\1.png")
        time.sleep(3)
        transfer = self.browser.find_element(*DispatchLocators.TRANSFER)
        transfer.click()





