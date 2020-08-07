from .pages.music_page import MusicPage



def test_guest_can_go_to_login_page(browser):
    link = "https://vk.com"
    page = MusicPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = MusicPage(browser, browser.current_url)  # переход происходит неявно, страницу инициализируем в теле
    # теста
    login_page.go_to_enter_login()
    login_page.go_to_enter_password()
    login_page.push_the_button()
    login_page.go_to_the_music_page()
    login_page.go_to_the_search()
    login_page.go_to_the_result()



