import os
import pytest
import json
from datetime import datetime
from checker import Binance, Kucoin

# Создаем экземпляры классов
binance = Binance()
kucoin = Kucoin()

def clean_file():
    # Очищаем файл перед началом тестов
    if os.path.exists('price_differences.json'):
        with open('price_differences.json', 'w') as f:
            f.write('[]')  # Записываем пустой список в файл

def save_to_json(data):
    # Проверяем, существует ли файл и не пустой ли он
    if os.path.exists('price_differences.json') and os.path.getsize('price_differences.json') > 0:
        # Если файл существует и не пустой, загружаем существующие данные
        with open('price_differences.json', 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []  # Если файл пустой или не существует, создаем новый список

    # Добавляем новые данные
    existing_data.append(data)

    # Сохраняем обновленные данные обратно в файл
    with open('price_differences.json', 'w') as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)  # Записываем весь массив обратно в файл

@pytest.fixture(scope="module", autouse=True)
def setup_module():
    clean_file()  # Очищаем файл перед началом тестов

@pytest.mark.parametrize("name_coin", ["BTC", "ETH", 'SOL', "LTC", 'NOT'])  # Параметризация для разных монет
def test_price_comparison(name_coin):
    # Получаем цены с использованием методов из класса
    bin_price = binance.get_price(name_coin).get('price')
    kuk_price = kucoin.get_price(name_coin).get('data', {}).get('price')

    # Преобразуем в float для сравнения
    bin_price = float(bin_price) if bin_price is not None else None
    kuk_price = float(kuk_price) if kuk_price is not None else None

    # Проверяем, были ли получены цены
    if bin_price is not None and kuk_price is not None:
        dif: float = bin_price - kuk_price

        # Утверждение, что цены различаются
        if bin_price != kuk_price:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Форматируем дату и время
            data = {
                'name': name_coin,
                'price_binance': bin_price,
                'price_kucoin': kuk_price,
                'date_and_time': current_time
            }
            save_to_json(data)  # Перезаписываем данные в файл

            # Выводим информацию для отладки
            print(f"Цены различаются для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price} на {dif}")
            assert dif != 0, f"Цены должны различаться для {name_coin}, но они равны: {bin_price} и {kuk_price}"
        else:
            print(f"Цены совпадают для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}")
            # Здесь можно сделать вывод, что тест не должен проходить, если цены совпадают
            assert False, f"Цены совпадают для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}"
    else:
        pytest.fail(f"Не удалось получить цены для {name_coin}: Binance - {bin_price}, KuCoin - {kuk_price}")