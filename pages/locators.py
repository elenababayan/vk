from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#index_email")
    PASSWORD = (By.
                CSS_SELECTOR, "#index_pass")
    BUTTON = (By.CSS_SELECTOR, "#index_login_button")