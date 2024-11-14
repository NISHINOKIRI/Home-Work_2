import os
import pytest
import json
from datetime import datetime
from changed_checker import Binance, Kucoin

crypro_list = ["SOL"]  # Задаём тут список монеток которые хотим проверить

class TestClass:
    # Создаем экземпляры классов
    def setup_method(self):
        self.binance = Binance()
        self.kucoin = Kucoin()

    @staticmethod
    def clean_file():
        """Очищает файл price_differences.json перед запуском тестов."""
        with open('price_differences.json', 'w') as f:
            f.write('[]')  # Записываем пустой список в файл

    @staticmethod
    def save_to_json(data):
        """Сохраняет данные в файл price_differences.json."""
        if os.path.exists('price_differences.json') and os.path.getsize('price_differences.json') > 0:
            with open('price_differences.json', 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.append(data)

        with open('price_differences.json', 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

    @pytest.fixture(scope="module", autouse=True)
    def setup_module(self):
        """Фикстура для очистки файла перед запуском тестов."""
        self.clean_file()

    @pytest.mark.parametrize("name_coin", crypro_list)
    def test_trading_status(self, name_coin):
        """Тест на проверку статуса торговли между Binance и KuCoin."""
        print(f"Запуск теста статуса торговли для {name_coin}")

        # Приводим к правильному формату символ
        bin_symbol = name_coin.upper()  # Пример для Binance
        kucoin_symbol = name_coin.upper()  # Пример для KuCoin

        # Проверяем статус торговли
        bin_status = self.binance.get_status(bin_symbol)  # Предполагается, что возвращает True или False
        kucoin_status = self.kucoin.get_status(kucoin_symbol)  # Предполагается, что возвращает True или False

        # Проверка статуса торговли на Binance
        assert 'разрешена' in bin_status, f"Торговля для {bin_symbol} на Binance не активна: {bin_status}"

        # Проверка статуса торговли на KuCoin
        assert 'разрешена' in kucoin_status, f"Торговля для {kucoin_symbol} на KuCoin не активна: {kucoin_status}"

    @pytest.mark.parametrize("name_coin", crypro_list)
    def test_price_comparison(self, name_coin):
        """Тест на сравнение цен между Binance и KuCoin."""
        try:
            print(f"Запуск теста для {name_coin}")  # Используем print для вывода информации
            bin_price = self.binance.get_price(name_coin).get('price')
            kuk_price = self.kucoin.get_price(name_coin).get('data', {}).get('price')

            bin_price = float(bin_price) if bin_price is not None else None
            kuk_price = float(kuk_price) if kuk_price is not None else None

            if bin_price is not None and kuk_price is not None:
                dif = abs(bin_price - kuk_price)  # Находим абсолютное различие
                dif_rounded = round(dif, 7)  # Округляем разницу до 7 знаков после запятой

                if bin_price != kuk_price:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data = {
                        'different_price': 'pass',
                        'name': str(name_coin),
                        'price_binance': str(bin_price),
                        'price_kucoin': str(kuk_price),
                        'different_price_value': '≈ ' +  str(dif_rounded),
                        'date_and_time': str(current_time)
                    }
                    self.save_to_json(data)  # Сохраняем данные только если цены различаются

                    print(
                        f"Цены различаются для {name_coin}: Binance - {bin_price:.7f}, KuCoin - {kuk_price:.7f} (разница: {dif_rounded:.7f})")
                    assert dif_rounded != 0, f"Цены должны различаться для {name_coin}, но они равны: {bin_price} и {kuk_price}"
                else:
                    print(f"Цены совпадают для {name_coin}: Binance - {bin_price:.7f}, KuCoin - {kuk_price:.7f}")
                    assert False, f"Цены совпадают для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}"
            else:
                pytest.fail(f"Не удалось получить цены для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}")
        except Exception as e:
            print(f"Ошибка при получении цен для {name_coin}: {str(e)}")
            pytest.fail(f"Ошибка при получении цен для {name_coin}: {str(e)}")

    @pytest.mark.parametrize("symbol", crypro_list)
    def test_equality_trading_parameters_price_filter(self, symbol):
        """Тест на сравнение шагов цены торговых параметров между Binance и KuCoin."""
        self.compare_trading_parameters_(symbol, 'PRICE_FILTER')

    @pytest.mark.parametrize("symbol", crypro_list)
    def test_equality_trading_parameters_lot_size(self, symbol):
        """Тест на сравнение минимального размера торговых параметров между Binance и KuCoin."""
        self.compare_trading_parameters_(symbol, 'LOT_SIZE')

    def compare_trading_parameters_(self, symbol, filter_type):
        """Общая функция для сравнения торговых параметров."""
        binance_data = self.binance.get_data()
        kucoin_data = self.kucoin.get_data()

        binance_symbol_info = next(
            (item for item in binance_data['symbols'] if item['symbol'] == f'{symbol.upper()}USDT'), None)

        kucoin_symbol_info = next(
            (item for item in kucoin_data['data'] if item['symbol'] == f'{symbol.upper()}-USDT'), None)

        assert binance_symbol_info is not None, f"Символ {symbol.upper()}USDT не найден на Binance"
        assert kucoin_symbol_info is not None, f"Символ {symbol.upper()}-USDT не найден на KuCoin"

        if filter_type == 'LOT_SIZE':
            self.check_minimum_size_(binance_symbol_info, kucoin_symbol_info, symbol)
        elif filter_type == 'PRICE_FILTER':
            self.check_price_step(binance_symbol_info, kucoin_symbol_info, symbol)
        else:
            pytest.fail(f"Неизвестный тип фильтра: {filter_type}")

    def check_minimum_size_(self, binance_symbol_info, kucoin_symbol_info, symbol):
        """Проверка минимальных размеров торговых параметров."""
        bin_min_qty = next(filter(lambda f: f['filterType'] == 'LOT_SIZE', binance_symbol_info['filters']), None)
        if bin_min_qty is None:
            pytest.fail(f"Не удалось найти фильтр LOT_SIZE для {symbol.upper()} на Binance")

        ku_min_qty = kucoin_symbol_info['baseMinSize']

        bin_min_qty_value = float(bin_min_qty['minQty'])
        ku_min_qty_value = float(ku_min_qty)

        if bin_min_qty_value != ku_min_qty_value:
            difference_min_qty = abs(bin_min_qty_value - ku_min_qty_value)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {
                'min_size_step_of_treading_status': 'pass',
                'name': str(symbol.upper()),
                'binance_min_qty': str(bin_min_qty_value),
                'kucoin_min_qty': str(ku_min_qty_value),
                'difference': '≈ ' + str(difference_min_qty),
                'date_and_time': str(current_time)
            }
            self.save_to_json(data)

        assert bin_min_qty_value == ku_min_qty_value, f"Минимальный размер на KuCoin не совпадает с Binance для {symbol.upper()}"

    def check_price_step(self, binance_symbol_info, kucoin_symbol_info, symbol):
        """Проверка шагов цены торговых параметров."""
        bin_price_filter = next(filter(lambda f: f['filterType'] == 'PRICE_FILTER', binance_symbol_info['filters']),
                                None)
        if bin_price_filter is None:
            pytest.fail(f"Не удалось найти фильтр PRICE_FILTER для {symbol.upper()} на Binance")

        ku_price_increment = kucoin_symbol_info.get('priceIncrement')
        if ku_price_increment is None:
            pytest.fail(f"Не удалось получить priceIncrement для {symbol.upper()} на KuCoin")

        bin_tick_size_value = float(bin_price_filter['tickSize'])
        ku_tick_size_value = float(ku_price_increment)

        # Преобразование значений в строку без научной нотации
        bin_tick_size_str = f"{bin_tick_size_value:.7f}"
        ku_tick_size_str = f"{ku_tick_size_value:.7f}"
        difference_tick_size = abs(bin_tick_size_value - ku_tick_size_value)

        # Преобразование разницы в строку без научной нотации
        difference_tick_size_str = f'{difference_tick_size:.7f}'

        if bin_tick_size_value != ku_tick_size_value:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {
                'min_step_price_different': 'pass',
                'name': str(symbol.upper()),
                'binance_tick_size': str(bin_tick_size_str),
                'kucoin_tick_size': str(ku_tick_size_str),
                'difference_tick_size': '≈ ' + str(difference_tick_size_str),
                'date_and_time': str(current_time)
            }
            self.save_to_json(data)

        assert bin_tick_size_value == ku_tick_size_value, f"Шаг цены на KuCoin не совпадает с Binance для {symbol.upper()}"
