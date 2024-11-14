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

    @staticmethod
    def get_proceed_data(data, symbol):
        printing_symbol = f'{symbol}'
        # Автоматически добавляем USDT к символу
        full_symbol = f'{symbol.upper()}USDT'
        print("------------------------------------------------")
        print("------------------------------------------------")
        print("Данные от Binance:")
        print(f"Информация о монете {printing_symbol}:")

        # Проверяем, есть ли ключ 'symbols' в данных
        if 'symbols' not in data:
            print("Ошибка: Неверный ответ от API или отсутствует 'symbols'")
            return

        for item in data['symbols']:
            if item['symbol'] == full_symbol:
                print("------------------------------------------------")
                print(f"Базовая валюта: {item['baseAsset']}")
                print(f"Котируемая валюта: {item['quoteAsset']}")

                # Получаем фильтры для минимального и максимального размера
                min_qty = next(filter(lambda f: f['filterType'] == 'LOT_SIZE', item['filters']), None)
                min_notional = next(filter(lambda f: f['filterType'] == 'NOTIONAL', item['filters']), None)
                price_filter = next(filter(lambda f: f['filterType'] == 'PRICE_FILTER', item['filters']), None)

                if min_qty:
                    print(f"Минимальный размер: {min_qty['minQty']} {item['baseAsset']}")
                    print(f"Максимальный размер: {min_qty['maxQty']} {item['baseAsset']}")
                if price_filter:
                    print(f"Шаг цены: {price_filter['tickSize']} {item['quoteAsset']}")
                if min_notional:
                    print(f"Минимальные средства: {min_notional['minNotional']} {item['quoteAsset']}")

                print(f"Возможность маржинальной торговли: {'Да' if item['isMarginTradingAllowed'] else 'Нет'}")
                print(f"Торговля включена: {'Да' if item['status'] == 'TRADING' else 'Нет'}")
                print("------------------------------------------------")
                break
        else:
            print(f"Символ {symbol.upper()} не найден.")

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

    @staticmethod
    def get_proceed_data(data, symbol):
        printing_symbol = f'{symbol}'
        # Формируем полный символ
        full_symbol = f'{symbol.upper()}-USDT'
        print("------------------------------------------------")
        print("------------------------------------------------")
        print("Данные от Kucoin:")
        print(f"Информация о монете {printing_symbol}:")

        # Проверяем, есть ли ключ 'data' в данных
        if 'data' not in data:
            print("Ошибка: Неверный ответ от API или отсутствует 'data'")
            return

        for item in data['data']:
            if item['symbol'] == full_symbol:
                print("------------------------------------------------")
                print(f"Базовая валюта: {item['baseCurrency']}")
                print(f"Котируемая валюта: {item['quoteCurrency']}")
                print(f"Минимальный размер: {item['baseMinSize']} {item['baseCurrency']}")
                print(f"Максимальный размер: {item['baseMaxSize']} {item['baseCurrency']}")
                print(f"Шаг цены: {item['priceIncrement']} {item['quoteCurrency']}")
                print(f"Минимальные средства: {item['minFunds']} {item['quoteCurrency']}")
                print(f"Возможность маржинальной торговли: {'Да' if item['isMarginEnabled'] else 'Нет'}")
                print(f"Торговля включена: {'Да' if item['enableTrading'] else 'Нет'}")
                print("------------------------------------------------")
                break
        else:
            print(f"Символ {full_symbol} не найден.")