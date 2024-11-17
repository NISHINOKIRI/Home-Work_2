# Токен и ник нужно подсталять свой) Токен который указан тут уже недействительный)

import requests

# Определяем цвета
class Colors:
    RESET = "\033[0m"  # Сброс цвета
    GREEN = "\033[92m"  # Зеленый цвет
    RED = "\033[91m"    # Красный цвет

def github_api_auth(url, actual_token):
    headers = {
        'Authorization': f'token {actual_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(f'{url}/user', headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(f'{Colors.GREEN}Authorization has been passed{Colors.RESET}')  # Зеленый цвет
    else:
        print(f'{Colors.RED}Failed to authenticate: {response.status_code}{Colors.RESET}')  # Красный цвет


def authenticate(nickname, url, actual_token):
    headers = {
        'Authorization': f'token {actual_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(f'{url}/user', headers=headers)
    user_data = response.json()

    if response.status_code == 200 and user_data['login'] == nickname:
        user_data = response.json()
        print(f'{Colors.GREEN}Authenticated as: {user_data["login"]}{Colors.RESET}')  # Зеленый цвет
    else:
        print(f'{Colors.RED}Failed\nError status-code: {response.status_code}\nOr login is not equal {nickname}{Colors.RESET}')  # Красный цвет

# Вызов функции для аутентификации
github_api_auth('https://api.github.com', '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')
# Вызов функции для проверки совпадения никнейма\логина
authenticate('NISHINOKIRI', 'https://api.github.com', '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')
