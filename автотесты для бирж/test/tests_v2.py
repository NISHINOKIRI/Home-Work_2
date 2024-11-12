import os
import pytest
import json
from datetime import datetime
from checker import Binance, Kucoin


class TestClass:
    # Создаем экземпляры классов
    def setup_method(self):
        self.binance = Binance()
        self.kucoin = Kucoin()

    def clean_file(self):
        """Очищает файл price_differences.json перед запуском тестов."""
        with open('price_differences.json', 'w') as f:
            f.write('[]')  # Записываем пустой список в файл

    def save_to_json(self, data):
        """Сохраняет данные в файл price_differences.json."""
        if os.path.exists('price_differences.json') and os.path.getsize('price_differences.json') > 0:
            with open('price_differences.json', 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.append(data)

        with open('price_differences.json', 'w') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)

    @pytest.fixture(scope="module", autouse=True)
    def setup_module(self):
        """Фикстура для очистки файла перед запуском тестов."""
        self.clean_file()

    @pytest.mark.parametrize("name_coin", ["BTC", "ETH", "SOL", "LTC", "NOT"])
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

    @pytest.mark.parametrize("name_coin", ["BTC", "ETH", "SOL", "LTC", "NOT"])
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
                dif_rounded = round(dif, 6)  # Округляем разницу до 6 знаков после запятой

                if bin_price != kuk_price:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data = {
                        'name': name_coin,
                        'price_binance': bin_price,
                        'price_kucoin': kuk_price,
                        'date_and_time': current_time
                    }
                    self.save_to_json(data)  # Сохраняем данные только если цены различаются

                    print(
                        f"Цены различаются для {name_coin}: Binance - {bin_price:.6f}, KuCoin - {kuk_price:.6f} (разница: {dif_rounded:.6f})")
                    assert dif_rounded != 0, f"Цены должны различаться для {name_coin}, но они равны: {bin_price} и {kuk_price}"
                else:
                    print(f"Цены совпадают для {name_coin}: Binance - {bin_price:.6f}, KuCoin - {kuk_price:.6f}")
                    assert False, f"Цены совпадают для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}"
            else:
                pytest.fail(f"Не удалось получить цены для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}")
        except Exception as e:
            print(f"Ошибка при получении цен для {name_coin}: {str(e)}")
            pytest.fail(f"Ошибка при получении цен для {name_coin}: {str(e)}")