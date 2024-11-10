import requests
import json
from Decor.Decor import Decs

class SwaggerPetID:
    def __init__(self):
        self.data = None

    @staticmethod
    def get_id_from_user(pet_id):
        while True:
            if pet_id.isdigit():
                return pet_id  # Возвращаем pet_id если это целое число
            else:
                print("Неверно!. ID может быть только целым числом!")
            return pet_id

    #@Decs.statuscode
    def request_processing(self, pet_id):
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        self.data = response.json()
        filename = f'Pet_ID_{pet_id}_info.json'
        # Вызов декоратора с нужным именем файла
        #Decs.save_to_json(filename)(lambda: response)()  # Вызов декоратора
        print('\nОбработанный ответ:')
        for key, value in self.data.items():
            print(f'{key}: {value}')
        return response

    def return_answer_json(self, pet_id):
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")

        if response.status_code == 200:
            self.data = response.json()
            print(f'Отлично!\nПитомец найден!\nДанные в джейсоне:')
            print(json.dumps(self.data, indent=2, ensure_ascii=False))
            return self.data
        else:
            print(f'Питомец с ID {pet_id} не найден или удалён')
            self.data = response.json()
            print('Данные в JSON:')
            print(json.dumps(self.data, indent=2, ensure_ascii=False))
            return self.data

    #@Decs.statuscode
    def dell(self, pet_id):
        response = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        if response.status_code == 200:
            print('Питомец успешно удалён.')
            filename = f'Pet_ID_{pet_id}_was_deleted.json'
            # Вызов декоратора с нужным именем файла
            #Decs.save_to_json(filename)(lambda: response)()  # Вызов декоратора
            return response  # Возвращаем объект ответа
        else:
            print(f'Не удалось удалить питомца с ID {pet_id}')
            return response # Возвращаем объект ответа

    #@Decs.statuscode
    def add_pet(self, id, name, category_name, status="available"):
        # Формируем данные о питомце
        pet_data = {
            "id": id,
            "category": {
                "id": 0,
                "name": category_name
            },
            "name": name,
            "photoUrls": ["string"],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": status
        }

        # Отправляем запрос для добавления питомца
        response = requests.post("https://petstore.swagger.io/v2/pet", json=pet_data)

        if response.status_code in [200, 201]:
            filename = f'Pet_ID_{pet_data["id"]}_was_added.json'
            # Вызов декоратора с нужным именем файла
            #Decs.save_to_json(filename)(lambda: response)()  # Вызов декоратора
            print(f'Питомец c ID {pet_data['id']} успешно добавлен.')
            return response  # Возвращаем объект ответа
        else:
            print(f'Не удалось добавить питомца.')
            return response  # Возвращаем объект ответа