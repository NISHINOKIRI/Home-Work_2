from checker import Binance, Kucoin
import datetime
import requests

# Глобальная переменная для имени монеты
name_coin = None # Её нужно будет передать в конце кода иначе не сработает! (ну или можно прям тут поменять тогда change_coin не нужно использовать)

def change_name_coin(new_coin):
    global name_coin  # Указываем, что мы хотим использовать глобальную переменную (ПОДСМОТРЕННО)
    name_coin = new_coin  # Меняем значение глобальной переменной (ПОСМОТРЕННО)

change_name_coin('BTC')  # устанавлдиваем имя монеты

bin = Binance()
kuk = Kucoin()

bin_price = bin.get_price(f'{name_coin}').get('price')
kuk_price = kuk.get_price(f'{name_coin}').get('data').get('price')


def price_info_in_usdt_about_all():
    print(f'\nДанные биржы Binance\nМонета: {name_coin}\nUSDT: {bin_price} \n')
    print(f'Данные биржы Kucoin\nМонета: {name_coin}\nUSDT: {kuk_price} \n')

def eq(eq):
    if bin_price is None or kuk_price is None:
        return False
    return bin_price == kuk_price

def check_equality_price():
    condition_result = eq(True)  # Передаем True для проверки
    if condition_result:
        result = 'Да'
    else:
        result = 'Нет'
    print(f'\nСтоимость монет совпадает на биржах - {result}')

def price_info(name_coin):
    coin = name_coin
    price_binance = bin.get_price(coin).get('price')
    price_kucoin = kuk.get_price(coin).get('data', {}).get('price')  # {} для предотвращения ошибки

    if price_binance is None or price_kucoin is None:
        print("Ошибка: Не удалось получить цены для монеты.")
        return {}

    current_time = datetime.datetime.now()
    date_n = current_time.strftime('%d.%m.%Y')
    time_n = current_time.strftime('%H:%M')
    date_and_time = f"{date_n} {time_n}"

    return {
        'name': coin,
        'binance_price': price_binance,
        'kucoin_price': price_kucoin,
        'date_and_time': date_and_time
    }

def print_price_info_processed():
    info = price_info(name_coin)
    print('Обработанный ответ:')
    print(f"Монета: {info['name']}")
    print(f"Цена на Binance: {info['binance_price']} USDT")
    print(f"Цена на Kucoin: {info['kucoin_price']} USDT")
    print(f"Дата и время запроса: {info['date_and_time']}")

def print_price_info_not_processed():
    info = price_info(name_coin)
    print(f'Необработанный ответ:\n{info}' + '\n')

def check_trading_status():
    print()
    print(f'На бирже Binance тогравля {name_coin}' + bin.get_status(f'{name_coin}'))
    print(f'На бирже Kucoin тогравля {name_coin}' + kuk.get_status(f'{name_coin}'))

check_equality_price()
price_info_in_usdt_about_all()
print_price_info_not_processed()
print_price_info_processed()
check_trading_status()



