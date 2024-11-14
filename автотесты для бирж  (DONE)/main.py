from Manage.Manage import Manage_Checker

"""Основная логика выполнения"""

checker = Manage_Checker('NOT')          # Создаем экземпляр класса для криптовалюты 'NOT' (ну или другого, достаточно просто переписать)
checker.check_equality_price()           # Проверяем равенство цен
checker.price_info_in_usdt_about_all()   # Выводим информацию о ценах на обеих биржах
checker.print_price_info_not_processed() # Выводим необработанную информацию о ценах  (по формату ТЗ)
checker.print_price_info_processed()     # Выводим обработанную информацию о ценах    (по формату ТЗ)
checker.check_trading_status()           # Проверяем статус торговли на обеих биржах
checker.get_proceed_data()               # Получаем и обрабатываем данные от обеих бирж

