from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#index_email")
    PASSWORD = (By.CSS_SELECTOR, "#index_pass")
    BUTTON = (By.CSS_SELECTOR, "#index_login_button")


class MessageLocators():
    MESSAGE = (By.XPATH, "//*[@id='l_msg']/a")


class DialogueLocators():
    DIALOGUUE = (By.CLASS_NAME, 'nim-dialog._im_dialog._im_dialog_2000000003.nim-dialog_unread-out.nim-dialog_classic')
    DIA = (By.CLASS_NAME, 'nim-dialog._im_dialog._im_dialog_2000000003.nim-dialog_unread-out.nim-dialog_classic')


class DispatchLocators():
    DISPATCH = (By.CSS_SELECTOR, "#im_editable0")
    TRANSFER = (By.CLASS_NAME, "im-send-btn.im-chat-input--send._im_send.im-send-btn_send")


class MusicLocators():
    MUSIC = (By.XPATH, '//*[@id="l_aud"]/a')
    SEARCH = (By.CSS_SELECTOR, "#audio_search")
    BUTTONSEARCH = (By.CLASS_NAME, "ui_search_button_search._ui_search_button_search")
    RESULT = (By.CLASS_NAME, "audio_row__title_inner._audio_row__title_inner")

    # TODO: лучше реже использовать теги
    PLAYER_ADD = (By.CLASS_NAME, "audio_page_player_btn.audio_page_player_add._audio_page_player_add")

    # TODO: неправильный селектор в классе пробел
    ADDED = (By.CLASS_NAME, "audio_row audio_row_with_cover._audio_row._audio_row_403478867_456239253.audio_can_add audio_has_thumb audio_row2")


class DownloadLocators():
    DOWNLOAD_PARENT = (By.CSS_SELECTOR, ".ms_item_more")
    # DOWNLOAD = (By.CSS_SELECTOR, ".ms_item.ms_item_photo._type_photo")
    # DOWNLOAD_TWO = (By.CSS_SELECTOR, "#photos_choose_upload_area_label")
    # DISPATCH = (By.CSS_SELECTOR, '.photos_choose_upload_area_upload')
    DISPATCH = (By.CSS_SELECTOR, '.im-dropbox--inputfile._im_upload_photo input')
