from typing import Any
import requests

class Binance:
    URL = 'https://api.binance.com/api/v3'

    def get_price(self, symbol: str) -> dict[str, Any]:
        url = f'{self.URL}/ticker/price'
        response = requests.get(url=url, params={'symbol': f'{symbol.upper()}USDT'})
        return response.json()

    def get_data(self) -> dict[str, Any]:
        url = f'{self.URL}/exchangeInfo'
        response = requests.get(url=url)
        return response.json()

    def get_status(self, symbol: str) -> str:
        data = self.get_data()  # Предполагается, что get_data() возвращает данные в нужном формате
        if 'symbols' in data and len(data['symbols']) > 0:
            target_symbol = f'{symbol.upper()}USDT'  # Формируем целевой символ без дефиса, так нужно для бинанса
            for item in data['symbols']:
                if item['symbol'] == target_symbol:  # Ищем нужный символ
                    status = item.get('status')  # Получаем статус
                    if status == 'TRADING':
                        return ' разрешена'
                    else:
                        return ' запрещена' # Если статус не TRADING
        return "Ошибка: Неверный ответ от API или отсутствует 'symbols'"

class Kucoin:
    URL = 'https://api.kucoin.com/api/v1'

    def get_price(self, symbol: str) -> dict[str, Any]:
        url = f'{self.URL}/market/orderbook/level1'
        response = requests.get(url=url, params={'symbol': f'{symbol.upper()}-USDT'})
        return response.json()

    def get_data(self) -> dict[str, Any]:
        url = f'{self.URL}/symbols'
        response = requests.get(url=url)
        return response.json()

    def get_status(self, symbol: str) -> str:
        data = self.get_data()

        if 'data' in data:
            target_symbol = f'{symbol.upper()}-USDT'
            for item in data['data']:
                if item['symbol'] == target_symbol:
                    # Проверяем поле enableTrading
                    trading_enabled = item.get('enableTrading', None)
                    if trading_enabled is not None:
                        return ' разрешена' if trading_enabled else ' запрещена'
        return "Ошибка: Неверный ответ от API или отсутствует 'data'"