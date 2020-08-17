from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#index_email")
    PASSWORD = (By.CSS_SELECTOR, "#index_pass")
    BUTTON = (By.CSS_SELECTOR, "#index_login_button")

class MessageLocators():
    MESSAGE = (By.XPATH, "//*[@id='l_msg']/a")

class DialogueLocators():
    DIALOGUUE = (By.XPATH, '//*[@id="im_dialogs"]/li[2]/div[2]/div/div[2]/span[1]/span')

class DispatchLocators():
    DISPATCH = (By.CSS_SELECTOR, "#im_editable0")
    TRANSFER = (By.CLASS_NAME,"im-send-btn.im-chat-input--send._im_send.im-send-btn_send")

class MusicLocators():
    MUSIC = (By.XPATH, '//*[@id="l_aud"]/a')
    SEARCH = (By.CSS_SELECTOR, "#audio_search")
    BUTTONSEARCH = (By.CLASS_NAME,"ui_search_button_search._ui_search_button_search")
    RESULT = (By.CSS_SELECTOR,".audio_section__search .audio_row__title_inner._audio_row__title_inner")
    ADDITION = (By.CLASS_NAME, "audio_page_player_btn.audio_page_player_add._audio_page_player_add")
    ADDED = (By.CLASS_NAME, "audio_page_player_btn.audio_page_player_add._audio_page_player_add audio_row__added audio_player_btn_added")

class DownloadLocators():
    DOWNLOAD = (By.CLASS_NAME,"ms_item.ms_item_photo._type_photo")
    DOWNLOAD_TWO = (By.CSS_SELECTOR, "#photos_choose_upload_area_label")


