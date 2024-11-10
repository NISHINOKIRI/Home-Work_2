from Decor.Decor import Decs
from utils.swagger import SwaggerPetID
import requests


class Manage:
    @staticmethod
    def request_info(id):
        swagger_pet = SwaggerPetID()  # Создаём экземпляр
        pet_id = id  # Получаем ID питомца
        swagger_pet.request_processing(pet_id)  # Получаем данные о питомце (если они есть в обработанном ответе)
        json_data = swagger_pet.return_answer_json(pet_id)  # Получаем JSON

    @staticmethod
    def dell(id):
        # Создаём экземпляр SwaggerPetID
        swagger_pet = SwaggerPetID()
        # Получаем ID питомца
        pet_id = id
        # Удаляем питомца
        response_data = swagger_pet.dell(pet_id)  # Выполняем удаление питомца

    @staticmethod
    def add(id, name, category_name, status):
        swagger_pet = SwaggerPetID()
        response_data = swagger_pet.add_pet(
            id=id,
            name=name,
            category_name=category_name,
            status=status)
        return response_data
