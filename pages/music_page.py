from .base_page import BasePage
from .locators import MusicLocators
from .locators import LoginPageLocators
import time
class MusicPage(BasePage):
    def go_to_enter_login(self):
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys('89094163112')

    def go_to_enter_password(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('Vfvjxrf908+')

    def push_the_button(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON)
        button.click()

    def go_to_the_music_page(self):
        music = self.browser.find_element(*MusicLocators.MUSIC)
        music.click()

    def go_to_the_search(self):
        search = self.browser.find_element(*MusicLocators.SEARCH)
        search.send_keys("Беспощадная")
        buttonsearch = self.browser.find_element(*MusicLocators.BUTTONSEARCH)
        buttonsearch.click()
        result = self.browser.find_element(*MusicLocators.RESULT)
        result.click()
        self.browser.refresh()

    def go_to_the_result(self):
        addition = self.browser.find_element(*MusicLocators.ADDITION)
        addition.click()
        assert self.browser.find_element(*MusicLocators.ADDED), "No melody added"