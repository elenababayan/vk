from .pages.message_form import MessageForm




def test_guest_can_go_to_message(browser):
    link = "https://vk.com/feed"
    page = MessageForm(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    message_page = MessageForm(browser, browser.current_url)  # переход происходит неявно, страницу инициализируем в теле
    # теста
    message_page.go_to_the_message()


