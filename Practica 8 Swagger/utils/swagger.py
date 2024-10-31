import requests
import json

class SwaggerPetID:
    def __init__(self):
        self.data = None

    @staticmethod
    def get_id_from_user():
        while True:
            pet_id = str(input('\nВведите ID питомца: '))
            if pet_id.isdigit():
                return pet_id # Возвращаем pet_id если это целое число
            else:
                print("Неверно!. ID может быть только целым числом!")

    def request_processing(self, pet_id):
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        if response.status_code == 200:
            # Тут не нужно снова делать запрос, данные уже получены в return_answer_json
            v = response.text
            data = json.loads(v)
            print('\n')
            print('Обработанный ответ:')
            for key, value in data.items():
                print(f'{key}: {value}')
        else:
            print(
                f'\nНевозможно получить данные о питомце с ID {pet_id}' + '\n')
            print(f'Статус код: {response.status_code}')

    def return_answer_json(self, pet_id):
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")

        if response.status_code == 200:  # Добавлена проверка на статус ответа
            self.data = response.json()  # Сохраняем данные в атрибуте экземпляра
            print(f'Отлично!\nПитомец найден\nCтатус-код - {response.status_code}\nДанные в джейсоне:')
            print(json.dumps(self.data, indent=2, ensure_ascii=False))  # Форматированный вывод JSON
            return self.data
        else:
            print(f'Невозможно получить данные о питомце с ID {pet_id}.\nОшибка - {response.status_code}')
            self.data = response.json()  # Сохраняем данные в атрибуте экземпляра
            print('Что-то пошло не так, но вот данные в джейсоне:')
            print(json.dumps(self.data, indent=2, ensure_ascii=False))  # Форматированный вывод JSON
            return self.data

    def run_all(self):
        # Получаем ID питомца
        pet_id = self.get_id_from_user()
        # Получаем данные о питомце
        self.return_answer_json(pet_id)
        # Обрабатываем данные
        self.request_processing(pet_id)
