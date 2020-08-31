import os
import time

from .base_page import BasePage
from .locators import DownloadLocators, MessageLocators, DialogueLocators, DispatchLocators

class DownloadPage(BasePage):

    def go_to_the_message(self):
        letter = self.browser.find_element(*MessageLocators.MESSAGE)
        letter.click()

    def go_to_the_page_dialogue(self):
        time.sleep(3)
        dialogue = self.browser.find_element(*DialogueLocators.DIA)
        dialogue.click()

    def go_to_the_download(self):
        time.sleep(3)
        downloadParent = self.browser.find_element(*DownloadLocators.DOWNLOAD_PARENT)
        downloadParent.click()
        # download = self.browser.find_element(*DownloadLocators.DOWNLOAD)
        # download.click()
        # download_two = self.browser.find_element(*DownloadLocators.DOWNLOAD_TWO)
        # download_two.click()
        dispatch = self.browser.find_element(*DownloadLocators.DISPATCH) #TODO: не здесь и плохой div div div ....
        dispatch.send_keys(os.getcwd() + "\\1.png")
        time.sleep(3)
        transfer = self.browser.find_element(*DispatchLocators.TRANSFER)
        transfer.click()





