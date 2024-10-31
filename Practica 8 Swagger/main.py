from utils.swagger import SwaggerPetID

#Автоматом
swagger_pet = SwaggerPetID() # Создаём экземпляр
swagger_pet.run_all()  # Запускаем все функции

# Или можно вручную
#swagger_pet = SwaggerPetID() # Создаём экземпляр
#pet_id = swagger_pet.get_id_from_user() # Получаем ID питомца
#swagger_pet.request_processing(pet_id)  # Получаем данные о питомце (если они есть в обработанном ответе)
#json_data = swagger_pet.return_answer_json(pet_id) # Получаем джейсон (стетем хе-хе )

