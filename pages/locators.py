from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.ID, "#quick_email")
    PASSWORD = (By.ID, "#quick_pass")
    BUTTON = (By.ID, "#quick_login_button")