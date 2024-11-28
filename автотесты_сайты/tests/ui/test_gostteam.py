import pytest
import allure
from lib.gostteam.page.gostteam_page import GostTeamPage
from lib.gostteam.page.gostteam_page import GostTeamPageWithBlog


@allure.feature('Тестирование сайта Gost Team')
class TestGostTeam:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, gost_team_page: GostTeamPage):
        self.page = gost_team_page

    @allure.story('Открытие главной страницы')
    def test_open_main_page(self):
        """Шаг 1: Открываем главную страницу."""
        with allure.step("Открываем главную страницу"):
            self.page.open_main_page()

        """Шаг 2: Проверяем, что элемент на странице не равен None."""
        with allure.step("Проверяем, что элемент не равен None"):
            element = self.page.open_main_page()
            assert element is not None, "Элемент не должен быть None"
            allure.attach("Элемент успешно загружен", name="Элемент", attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'open_main_page' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Переключение языка на английский')
    def test_main_page_switch_eng(self):
        """Шаг 1: Открываем главную страницу."""
        self.page.open_main_page()

        """Шаг 2: Переключаем язык на английский."""
        with allure.step("Переключаем язык на английский"):
            self.page.switch_to_eng()

        allure.attach("Тест 'main_page_switch_to_eng' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Получение стилей текста на главной странице')
    def test_main_page_get_color_text(self):
        """Шаг 1: Открываем главную страницу."""
        self.page.open_main_page()

        """Шаг 2: Переключаем язык на английский."""
        self.page.switch_to_eng()

        allure.attach("Тест 'main_page_get_color_text' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка открытия главной страницы')
    def test_styles(self):
        """Шаг 1: Открываем главную страницу."""
        self.page.open_main_page()

        allure.attach("Тест 'test_styles' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка наличия кнопки отправки на странице формы')
    def test_form_page_button_is_present(self):
        """Шаг 1: Открываем страницу формы тестов."""
        self.page.open_tests_form_page()

        """Шаг 2: Получаем кнопку отправки на русском языке."""
        element = self.page.sent_button_rus()  # Получаем элемент

        """Шаг 3: Проверяем, что элемент не равен None."""
        assert element is not None, "Элемент не должен быть None"
        allure.attach("Кнопка отправки успешно найдена", name="Кнопка отправки",
                      attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'test_form_page_button_is_present' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка текста кнопки отправки на русском')
    def test_form_page_button_tex_rus(self):
        """Шаг 1: Открываем страницу формы тестов."""
        self.page.open_tests_form_page()

        """Шаг 2: Получаем маску элемента."""
        element = self.page.masks()  # Получаем элемент

        """Шаг 3: Проверяем текст элемента."""
        assert element.text == "Оставить заявку", f"Ожидался текст 'Оставить заявку', но получен '{element.text}'"
        allure.attach(f"Текст кнопки: {element.text}", name="Текст кнопки", attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'form_page_button_text_rus' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка видимости кнопки отправки на русском')
    def test_sent_button_is_present(self):
        """Шаг 1: Открываем страницу формы тестов."""
        self.page.open_tests_form_page()

        """Шаг 2: Получаем кнопку отправки на русском языке."""
        self.page.sent_button_rus()

        """Шаг 3: Получаем маску элемента."""
        element = self.page.masks()  # Получаем элемент

        """Шаг 4: Проверяем роль элемента."""
        assert element.aria_role == 'none', f"Ожидалась роль элемента 'none', но получена '{element.aria_role}'"
        allure.attach(f"Полученная роль: {element.aria_role}", name="Роль элемента",
                      attachment_type=allure.attachment_type.TEXT)

        """Шаг 5: Проверяем текст элемента."""
        assert element.text == "Оставить заявку", f"Ожидался текст 'Оставить заявку', но получен '{element.text}'"
        allure.attach(f"Текст элемента: {element.text}", name="Текст элемента",
                      attachment_type=allure.attachment_type.TEXT)

        allure.attach("Элемент найден, тип элемента подтверждён", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка текста кнопки отправки на русском')
    def test_sent_button_text_is_correct_rus(self):
        """Шаг 1: Открываем страницу формы тестов."""
        self.page.open_tests_form_page()

        """Шаг 2: Получаем кнопку отправки на русском языке."""
        element = self.page.sent_button_rus()  # Получаем элемент

        """Шаг 3: Проверяем, что элемент не равен None."""
        assert element is not None, "Элемент не должен быть None"

        """Шаг 4: Проверяем текст элемента."""
        assert element.text == "Отправить", f"Ожидался текст 'Отправить', но получен '{element.text}'"
        allure.attach(f"Текст кнопки: {element.text}", name="Текст кнопки", attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'sent_button_text_is_correct_rus' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка текста кнопки отправки на английском')
    def test_sent_button_text_is_correct_eng(self):
        """Шаг 1: Открываем страницу формы тестов."""
        self.page.open_tests_form_page()

        """Шаг 2: Переключаем язык на английский."""
        self.page.switch_to_eng()

        """Шаг 3: Получаем кнопку отправки на английском языке."""
        element = self.page.sent_button_eng()  # Получаем элемент

        """Шаг 4: Проверяем, что элемент не равен None."""
        assert element is not None, "Элемент не должен быть None"

        """Шаг 5: Проверяем текст элемента."""
        assert element.text == "Send", f"Ожидался текст 'Send', но получен '{element.text}'"
        allure.attach(f"Текст кнопки: {element.text}", name="Текст кнопки", attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'sent_button_text_is_correct_eng' прошел успешно", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)


@allure.feature('Тестирование сайта Gost Team с блогом (страницы блога)')
class TestGostTeamPageWithBlog:
    @pytest.fixture(autouse=True)
    def setup(self, gost_team_page_with_blog: GostTeamPageWithBlog):
        self.page = gost_team_page_with_blog

    @allure.story('Открытие страницы блога')
    def test_blog_page(self):
        """Шаг 1: Открываем страницу блога."""
        self.page.open_blog_page()

        """Шаг 2: Получаем элемент на странице блога."""
        element = self.page.open_blog_page()  # Получаем элемент

        """Шаг 3: Проверяем, что элемент не равен None."""
        assert element is not None, "Элемент не должен быть None"
        allure.attach("Элемент успешно загружен", name="Элемент", attachment_type=allure.attachment_type.TEXT)

        allure.attach(f"Полученный элемент: {element.text.upper()}", name="Результат",
                      attachment_type=allure.attachment_type.TEXT)

    @allure.story('Проверка поля для ввода email')
    def test_mail_field(self):
        """Шаг 1: Открываем страницу блога."""
        self.page.open_blog_page()

        """Шаг 2: Получаем поле для ввода email."""
        element = self.page.mail_field()  # Получаем элемент

        """Шаг 3: Проверяем роль элемента."""
        assert element.aria_role == "textbox", f"Ожидалась роль 'textbox', но получена '{element.aria_role}'"
        allure.attach(f"Полученная роль: {element.aria_role}", name="Роль элемента",
                      attachment_type=allure.attachment_type.TEXT)

        allure.attach("Тест 'mail_field' прошел успешно", name="Результат", attachment_type=allure.attachment_type.TEXT)
