from .pages.download_page import DownloadPage


def test_guest_can_go_to_download_page(browser):
    link = "https://vk.com"
    page = DownloadPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = DownloadPage(browser, browser.current_url)
    login_page.go_to_enter_login()
    login_page.go_to_enter_password()
    login_page.push_the_button()
    login_page.go_to_the_message()
    login_page.go_to_the_page_dialogue()
    login_page.go_to_the_download()
