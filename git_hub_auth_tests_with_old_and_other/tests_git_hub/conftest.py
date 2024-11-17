import requests
import pytest

# Определяем цвета
class Colors:
    RESET = "\033[0m"  # Сброс цвета
    GREEN = "\033[92m"  # Зеленый цвет (для выделения пасов)
    YELLOW = "\033[93m"  # Жёлтый цвет (для выделения ошибок)

url = 'https://api.github.com'
token = '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'

# Определяем класс AuthResponse, который будет использоваться для хранения данных авторизации
class AuthResponse:
    pass  # Пустой класс, будет заполнен после авторизации

# Функция для авторизации через GitHub API
def github_api_auth(url, token):
    # Заголовки для запроса, включая токен
    headers = {
        'Authorization': f'token {token}',  # Используем токен для авторизации
        'Accept': 'application/vnd.github.v3+json'  # Указываем, что ожидаем ответ в формате JSON
    }

    # Выполняем GET-запрос к GitHub API для получения информации о пользователе
    response = requests.get(f'{url}/user', headers=headers)

    # Создаем экземпляр AuthResponse для хранения результатов авторизации
    auth_response = AuthResponse()

    # Проверяем статус-код ответа
    if response.status_code == 200:  # Если 200, авторизация успешна
        auth_response.status_code = response.status_code  # Сохраняем статус-код
        auth_response.user_data = response.json()  # Преобразуем ответ в JSON и сохраняем данные пользователя
        print()
        print(f'{Colors.GREEN}Авторизация пройдена успешно!{Colors.RESET}')  # Сообщаем об успешной авторизации
    else:  # Если статус-код не 200 / авторизация не удалась
        auth_response.status_code = response.status_code  # Сохраняем статус-код ошибки
        auth_response.user_data = None  # Устанавливаем user_data в None, так как данных нет
        print()
        print(f'{Colors.YELLOW}Авторизация не пройдена! Статус-код запроса: {response.status_code}{Colors.RESET}')  # Сообщаем об ошибке, выводим статус-код

    return auth_response  # Возвращаем объект AuthResponse с результатами авторизации

# Фикстура pytest, которая будет выполняться один раз за сессию тестирования
@pytest.fixture(scope='session')
def session_auth():
    return github_api_auth(url, token)  # Выполняем авторизацию и возвращаем объект AuthResponse