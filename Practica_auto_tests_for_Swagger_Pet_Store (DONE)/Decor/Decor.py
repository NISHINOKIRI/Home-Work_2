import json
class Decs:
    @staticmethod
    def statuscode(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'\nЭто отработал декоратор!\nСтатус-код: {result.status_code}\n')
            return result
        return wrapper

    @staticmethod
    def save_to_json(filename):
        """Декоратор для сохранения данных в файл формата JSON."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Вызываем основную функцию и получаем результат
                result = func(*args, **kwargs)
                data_to_save = result.json()  # Получаем данные из ответа
                with open(filename, 'w', encoding='utf-8') as json_file:
                    json.dump(data_to_save, json_file, ensure_ascii=False, indent=2)
                    print(f'Результаты сохранены в {filename}')
                return result  # Возвращаем результат
            return wrapper
        return decorator