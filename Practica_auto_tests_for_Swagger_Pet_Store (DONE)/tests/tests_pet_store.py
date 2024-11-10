import pytest
from manage.manage import Manage
from manage.manage import SwaggerPetID  # Импорт
pet = SwaggerPetID()
petm = Manage()

class TestPetStore:
        # Атрибут для хранения ID питомца
        pet_id = 33  # да.да, теперь его помжно поменять и запуститься тут, или передать в мейне но уже в экземпляр класса TestPetStore

        @pytest.fixture(scope="module")
        def pet_id_fixture(self):
                return self.pet_id  # Возвращаем ID питомца

        def test_create_pet(self, pet_id_fixture):
                petm.add(id=pet_id_fixture, name=str(pet_id_fixture), category_name='from_test', status='for_test') #создаём
                response = pet.request_processing(pet_id_fixture)
                assert response.status_code == 200

        def test_request_info_status_code(self, pet_id_fixture):
                # Дёргаем request_processing для получения инфо
                response = pet.request_processing(pet_id_fixture)
                # Чеки параметров
                assert response.status_code == 200
                assert response.json().get("id") == pet_id_fixture
                assert response.json().get("name") == str(pet_id_fixture)
                assert response.json().get("category").get("name") == 'from_test'
                assert response.json().get("status") == 'for_test'

        def test_first_del_pet(self, pet_id_fixture):
                # Удаляем питомца
                delete_response = pet.dell(pet_id_fixture)
                assert delete_response.status_code == 200

        def test_confirm_del_exist_pet(self, pet_id_fixture):
                # Запрашиваем информацию о питомце после его удаления
                response = pet.request_processing(pet_id_fixture)
                # Ожидаем, что питомец не найден, так что статус-код должен быть 404
                assert response.status_code == 404

        def test_PET_WAS_NOT_FOUND(self, pet_id_fixture):
                response = pet.request_processing(pet_id_fixture)
                # assert response.status_code in [404, 500], f'Ожидался код 404, но получен {response.status_code}' #см. AssertionError:
                # assert "error" or 'unknown' in response.json().get("type")
                assert response.json().get("type") in ["error",'unknown']
                assert response.status_code in [404, 500]