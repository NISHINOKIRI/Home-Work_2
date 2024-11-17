# Токен и ник нужно подсталять свой) Токен который указан тут уже недействительный)

import requests  # Импортируем библиотеку для выполнения HTTP-запросов
import pytest  # Импортируем библиотеку для написания тестов

# Вводим данные (токен генерируется тут: https://github.com/settings/tokens)
TOKEN = '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' # Токен для авторизации в GitHub API
NICKNAME = 'NISHINOKIRI'  # Ожидаемый никнейм пользователя


# Фикстура для получения базового URL GitHub API
@pytest.fixture
def github_api():
    base_url = 'https://api.github.com'  # Базовый URL для API
    return base_url  # Возвращаем базовый URL


# Тест для проверки авторизации в GitHub API
def test_github_auth(github_api):
    headers = {
        'Authorization': f'token {TOKEN}',  # Заголовок с токеном для авторизации
        'Accept': 'application/vnd.github.v3+json'  # Указываем, что ожидаем ответ в формате JSON
    }

    # Выполняем GET-запрос к API для получения информации о пользователе
    response = requests.get(f'{github_api}/user', headers=headers)

    # Проверяем статус ответа
    assert response.status_code == 200  # Ожидаемый статус - 200 (успех)


# Тест для проверки ника пользователя
def test_github_nickname(github_api):
    headers = {
        'Authorization': f'token {TOKEN}',  # Заголовок с токеном для авторизации
        'Accept': 'application/vnd.github.v3+json'  # Ожидаемый формат ответа
    }

    # Выполняем GET-запрос к API для получения информации о пользователе
    response = requests.get(f'{github_api}/user', headers=headers)

    # Проверяем, что данные пользователя получены в формате JSON
    user_data = response.json()

    # Проверяем, что логин пользователя соответствует ожидаемому
    assert user_data['login'] == NICKNAME  # Сравниваем полученный логин с ожидаемым никнеймом
