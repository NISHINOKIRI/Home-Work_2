from changed_checker import Binance, Kucoin
from datetime import datetime

class Manage_Checker:
    def __init__(self, name_coin):
        self.name_coin = name_coin        # Устанавливаем имя монеты
        self.bin = Binance()              # Создаем экземпляр класса Binance для работы с этой биржей
        self.kuk = Kucoin()               # Создаем экземпляр класса Kucoin для работы с этой биржей
        self.bin_price = None             # Переменная для цены на Binance
        self.kuk_price = None             # Переменная для цены на Kucoin

    def fetch_prices(self):
        """Получаем текущие цены для заданной криптовалюты на обеих биржах."""
        self.bin_price = self.bin.get_price(self.name_coin).get('price')                  # Получаем цену на Binance
        self.kuk_price = self.kuk.get_price(self.name_coin).get('data', {}).get('price')  # Получаем цену на Kucoin

    def price_info_in_usdt_about_all(self):
        """Выводим информацию о ценах на обеих биржах в USDT."""
        print(f'\nДанные биржы Binance\nМонета: {self.name_coin}\nUSDT: {self.bin_price} \n')
        print(f'Данные биржы Kucoin\nМонета: {self.name_coin}\nUSDT: {self.kuk_price} \n')

    def eq(self):
        """Проверяем, равны ли цены на обеих биржах."""
        if self.bin_price is None or self.kuk_price is None:        # Если хотя бы одна цена не была получена
            return False  # Цены не равны
        return self.bin_price == self.kuk_price                     # Возвращаем результат сравнения цен

    def check_equality_price(self):
        """Проверяем равенство цен на обеих биржах и выводим результат."""
        self.fetch_prices()                                         # Сначала получаем актуальные цены
        condition_result = self.eq()                                # Проверяем равенство цен
        result = 'Да' if condition_result else 'Нет'                # Определяем результат
        print(f'\nСтоимость монет совпадает на биржах - {result}')  # Выводим результат проверки

    def price_info(self):
        """Получаем информацию о ценах и времени запроса для заданной криптовалюты."""
        price_binance = self.bin.get_price(self.name_coin).get('price')                 # Получаем цену на Binance
        price_kucoin = self.kuk.get_price(self.name_coin).get('data', {}).get('price')  # Получаем цену на Kucoin

        if price_binance is None or price_kucoin is None:          # Если не удалось получить цены
            print("Ошибка: Не удалось получить цены для монеты.")  # Сообщаем об ошибке
            return {}  # Возвращаем пустой словарь

        current_time = datetime.now()  # Получаем текущее время
        date_and_time = current_time.strftime('%d.%m.%Y %H:%M')    # Форматируем дату и время
        return {                                                   # Возвращаем информацию о ценах и времени запроса
            'name': self.name_coin,
            'binance_price': price_binance,
            'kucoin_price': price_kucoin,
            'date_and_time': date_and_time
        }

    def print_price_info_processed(self):
        """Выводим обработанную информацию о ценах на обеих биржах."""
        info = self.price_info()  # Получаем информацию о ценах
        if info:                  # Если информация получена
            print('Обработанный ответ:')
            print(f"Монета: {info['name']}")
            print(f"Цена на Binance: {info['binance_price']} USDT")
            print(f"Цена на Kucoin: {info['kucoin_price']} USDT")
            print(f"Дата и время запроса: {info['date_and_time']}")

    def print_price_info_not_processed(self):
        """Выводим необработанную информацию о ценах."""
        info = self.price_info()                        # Получаем информацию о ценах
        print(f'Необработанный ответ:\n{info}' + '\n')  # Выводим необработанный ответ

    def check_trading_status(self):
        """Проверяем статус торговли на обеих биржах для заданной криптовалюты."""
        print()
        print(f'На бирже Binance торговля {self.name_coin}: {self.bin.get_status(self.name_coin)}')  # Статус на Binance
        print(f'На бирже Kucoin торговля {self.name_coin}: {self.kuk.get_status(self.name_coin)}')   # Статус на Kucoin

    def get_proceed_data(self):
        """Получаем и обрабатываем данные от обеих бирж."""
        bin_data = self.bin.get_data()                          # Получаем данные от Binance
        self.bin.get_proceed_data(bin_data, self.name_coin)     # Обрабатываем данные для Binance
        kucoin_data = self.kuk.get_data()                       # Получаем данные от Kucoin
        self.kuk.get_proceed_data(kucoin_data, self.name_coin)  # Обрабатываем данные для Kucoin
