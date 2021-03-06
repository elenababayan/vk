import time
from .pages.login_form import LoginForm


def test_guest_can_go_to_login_page(browser):
    link = "https://vk.com"
    page = LoginForm(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = LoginForm(browser, browser.current_url)  # переход происходит неявно, страницу инициализируем в теле
    # теста
    login_page.go_to_enter_login()
    login_page.go_to_enter_password()
    login_page.push_the_button()
    time.sleep(5)
    login_page.go_to_the_message()
    time.sleep(3)
    login_page.go_to_the_page_dialogue()
    login_page.sending_a_message()

