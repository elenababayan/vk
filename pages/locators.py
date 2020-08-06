from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#index_email")
    PASSWORD = (By.CSS_SELECTOR, "#index_pass")
    BUTTON = (By.CSS_SELECTOR, "#index_login_button")

class MessageLocators():
    MESSAGE = (By.XPATH, "//*[@id='l_msg']/a")

class DialogueLocators():
    DIALOGUUE = (By.XPATH, '//*[@id="im_dialogs"]/li[6]/div[2]/div')

class DispatchLocators():
    DISPATCH = (By.CSS_SELECTOR, "#im_editable0")
    TRANSFER = (By.CLASS_NAME,"im-send-btn.im-chat-input--send._im_send.im-send-btn_send")