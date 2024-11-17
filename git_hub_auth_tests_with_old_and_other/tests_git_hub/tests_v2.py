import pytest  # Импортируем библиотеку pytest для написания тестов
from pprint import pprint  # Импортируем pprint для красивого вывода

# Определяем цвета
class Colors:
    RESET = "\033[0m"  # Сброс цвета
    GREEN = "\033[92m"  # Зеленый цвет (для выделения пасов)
    YELLOW = "\033[93m"  # Жёлтый цвет (для выделения ошибок)
    PURPLE = "\033[95m"  # Фиолетовый цвет (для выделения инвалидного логина)
    INFO = "\033[38;5;04m"  # Сине-голубой цвет (для данных юзера)

# Указываем никнейм\логин для проверок
nickname = 'NISHINOKIRI'

# Тест для проверки статус-кода авторизации
@pytest.mark.usefixtures("session_auth")  # Указываем, что для этого теста будет использоваться фикстура session_auth
def test_user_authentication_status_code(session_auth):
    # Проверяем, что статус-код ответа равен 200 (успешная авторизация)
    assert session_auth.status_code == 200, f'{Colors.YELLOW}Ошибка: статус-код запроса к API - {session_auth.status_code}. Ожидался 200.{Colors.RESET}'
    print(f'{Colors.GREEN}Статус-код авторизации успешен: {session_auth.status_code}.{Colors.RESET}')  # Успешный вывод

# Тест для проверки получения данных пользователя
@pytest.mark.usefixtures("session_auth")  # Указываем, что для этого теста будет использоваться фикстура session_auth
def test_user_data_is_not_None(session_auth):
    # Проверяем, что user_data не равен None (авторизация прошла успешно и данные получены)
    assert session_auth.user_data is not None, f'{Colors.YELLOW}Ошибка: session_auth.user_data = None. Авторизация не прошла успешно.{Colors.RESET}'
    print(f'{Colors.GREEN}Данные пользователя успешно получены.{Colors.RESET}')  # Успешный вывод
    # Используем pprint для красивого отображения данных пользователя

    # Извлекаем данные пользователя
    user_data = {
        'login': session_auth.user_data.get('login'),
        'id': session_auth.user_data.get('id'),
        'followers': session_auth.user_data.get('followers'),
        'following': session_auth.user_data.get('following'),
        'public_repos': session_auth.user_data.get('public_repos'),
        'created_at': session_auth.user_data.get('created_at'),
        'updated_at': session_auth.user_data.get('updated_at'),
        'type': session_auth.user_data.get('type'),
        'plan': session_auth.user_data['plan']['name']  # plan сохраняем, но не выводим его в цикле
    }

    # Форматированный вывод
    print(f'{Colors.INFO}\nДанные пользователя{Colors.RESET}')
    for key, value in user_data.items():
        if key != 'plan':  # Пропускаем вывод 'plan'
            print(f'{key}: {value}')

    # Блок "ссылки"
    print(f'{Colors.INFO}\nСсылки{Colors.RESET}')
    print(f'avatar: {session_auth.user_data.get("avatar_url")}')
    print(f'profile: {session_auth.user_data.get("html_url")}')

    # Отдельный вывод для плана
    print(f'{Colors.INFO}\nИспользуемая подписочная модель{Colors.RESET}')
    print(f'{user_data["plan"]}')

# Тест для проверки поля "login" в данных пользователя
@pytest.mark.usefixtures("session_auth")  # Указываем, что для этого теста будет использоваться фикстура session_auth
def test_user_login(session_auth):
    # Проверяем, что поле "login" присутствует в данных пользователя
    assert 'login' in session_auth.user_data, f'{Colors.YELLOW}Ошибка: session_auth.user_data не содержит поле "login".{Colors.RESET}'

    # Извлекаем значение логина из данных пользователя
    login_value = session_auth.user_data.get('login')
    expected_login = nickname  # Замените на ваш никнейм; также добавьте актуальный токен в .tests_git_hub/conftest/github_api_auth

    # Проверяем, что login_value не равен None перед сравнением
    assert login_value is not None, f'{Colors.YELLOW}Ошибка: login_value = None. Логин не найден.{Colors.RESET}'

    # Проверяем, что полученный логин соответствует ожидаемому
    assert login_value == expected_login, f'{Colors.YELLOW}Ошибка: получен неверный логин - {Colors.PURPLE}{login_value}{Colors.RESET}'
    print(f'Получен ожидаемый логин: {Colors.GREEN}{login_value}.{Colors.RESET}')  # Успешный вывод

