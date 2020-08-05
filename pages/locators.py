from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#index_email")
    PASSWORD = (By.CSS_SELECTOR, "#index_pass")
    BUTTON = (By.CSS_SELECTOR, "#index_login_button")

class MessageLocators():
    MESSAGE = (By.CSS_SELECTOR, "#l_msg.a.span.span.left_label.inl_bl")
