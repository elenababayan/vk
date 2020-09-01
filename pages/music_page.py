from .base_page import BasePage
from .locators import MusicLocators
import time

class MusicPage(BasePage):

    def go_to_the_music_page(self):
        music = self.browser.find_element(*MusicLocators.MUSIC)
        music.click()

    def go_to_the_search(self):
        search = self.browser.find_element(*MusicLocators.SEARCH)
        search.send_keys("Беспощадная")
        buttonsearch = self.browser.find_element(*MusicLocators.BUTTONSEARCH)
        buttonsearch.click()

    def go_to_the_result(self):
        result = self.browser.find_element(*MusicLocators.RESULT)
        result.click()
        addition = self.browser.find_element(*MusicLocators.PLAYER_ADD)
        addition.click()
        self.browser.refresh()
        time.sleep(3)
        assert self.browser.find_element(*MusicLocators.ADDED), "No melody added"