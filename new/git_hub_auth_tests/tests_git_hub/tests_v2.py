from symtable import Class
import pytest  # Импортируем библиотеку pytest для написания тестов
from pprint import pprint  # Импортируем pprint для красивого вывода
from git_hub_auth_tests.tests_git_hub.conftest import github_api_auth
import allure

# Указываем никнейм\логин для проверок
nickname = 'NISHINOKIRI'
url = 'https://api.github.com'
token = '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'

# Определяем цвета
class Colors:
    RESET = "\033[0m"  # Сброс цвета
    GREEN = "\033[92m"  # Зеленый цвет (для выделения пасов)
    YELLOW = "\033[93m"  # Жёлтый цвет (для выделения ошибок)
    PURPLE = "\033[95m"  # Фиолетовый цвет (для выделения инвалидного логина)
    INFO = "\033[38;5;04m"  # Сине-голубой цвет (для данных юзера)

@allure.epic('TEST GitHub API')
class Testing_Git_Auth:

    # Конструктор для использования github_api_auth (что бы не передавать в каждый тест)
    def setup_class(self):
        self.session = github_api_auth(url, token)

    # Тест для проверки статус-кода авторизации
    @allure.story('Тест для проверки статус-кода авторизации')
    def test_user_authentication_status_code(self):
        # Проверяем, что статус-код ответа равен 200 (успешная авторизация)
        assert self.session.status_code == 200, f'{Colors.YELLOW}Ошибка: статус-код запроса к API - {self.session.status_code}. Ожидался 200.{Colors.RESET}'
        print(f'{Colors.GREEN}Статус-код авторизации успешен: {self.session.status_code}.{Colors.RESET}')  # Успешный вывод

    # Тест для проверки получения данных пользователя
    @allure.story('Тест для проверки получения данных пользователя')
    def test_user_data_is_not_None(self):
        # Проверяем, что user_data не равен None (авторизация прошла успешно и данные получены)
        assert self.session.user_data is not None, f'{Colors.YELLOW}Ошибка: self.session.user_data = None. Авторизация не прошла успешно.{Colors.RESET}'
        print(f'{Colors.GREEN}Данные пользователя успешно получены.{Colors.RESET}')  # Успешный вывод
        # Используем pprint для красивого отображения данных пользователя

        # Извлекаем данные пользователя
        user_data = {
            'login': self.session.user_data.get('login'),
            'id': self.session.user_data.get('id'),
            'followers': self.session.user_data.get('followers'),
            'following': self.session.user_data.get('following'),
            'public_repos': self.session.user_data.get('public_repos'),
            'created_at': self.session.user_data.get('created_at'),
            'updated_at': self.session.user_data.get('updated_at'),
            'type': self.session.user_data.get('type'),
            'plan': self.session.user_data['plan']['name']  # plan сохраняем, но не выводим его в цикле
        }

        # Форматированный вывод
        print(f'{Colors.INFO}\nДанные пользователя{Colors.RESET}')
        for key, value in user_data.items():
            if key != 'plan':  # Пропускаем вывод 'plan'
                print(f'{key}: {value}')

        # Блок "ссылки"
        print(f'{Colors.INFO}\nСсылки{Colors.RESET}')
        print(f'avatar: {self.session.user_data.get("avatar_url")}')
        print(f'profile: {self.session.user_data.get("html_url")}')

        # Отдельный вывод для плана
        print(f'{Colors.INFO}\nИспользуемая подписочная модель{Colors.RESET}')
        print(f'{user_data["plan"]}')

    # Тест для проверки поля "login" в данных пользователя
    @allure.story('Тест для проверки поля "login" в данных пользователя')
    def test_user_login(self):
        # Проверяем, что поле "login" присутствует в данных пользователя
        assert 'login' in self.session.user_data, f'{Colors.YELLOW}Ошибка: self.session.user_data не содержит поле "login".{Colors.RESET}'

        # Извлекаем значение логина из данных пользователя
        login_value = self.session.user_data.get('login')
        expected_login = nickname  # Замените на ваш никнейм; также добавьте актуальный токен в .tests_git_hub/conftest/github_api_auth

        # Проверяем, что login_value не равен None перед сравнением
        assert login_value is not None, f'{Colors.YELLOW} Ошибка: login_value = None. Логин не найден.{Colors.RESET}'

        # Проверяем, что полученный логин соответствует ожидаемому
        assert login_value == expected_login, f'{Colors.YELLOW}Ошибка: получен неверный логин - {Colors.PURPLE}{login_value}{Colors.RESET}'
        print(f'Получен ожидаемый логин: {Colors.GREEN}{login_value}.{Colors.RESET}')  # Успешный вывод

