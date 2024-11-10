from tests.tests_pet_store import TestPetStore
from utils.swagger import SwaggerPetID
import datetime

# Задаём айдишник
pet_id = 333
# Создаём экземпляр
pet = SwaggerPetID()
# # Создаём экземпляр
run_tests = TestPetStore()
# Присваиваем нужный нам айди (да, нелогично что он выше но всё же)
run_tests.pet_id = pet_id

# Получаем время (что бы было красиво и понятно)
now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
results_file = f'test_results_{now}.txt' # Создание файла для записи результатов

# Запуск тестов с печатью статуса (подсмотренно)
# Тут все тесты по порядку, что бы отрабатывало как я задумал, но можно просто не запускать ненужные
test_methods = [
    "test_create_pet",
    "test_request_info_status_code",
    "test_first_del_pet",
    "test_confirm_del_exist_pet",
    "test_PET_NOT_FOUND"
]

#Записываем результаты и выводим в консоль
with open(results_file, 'w', encoding='utf-8') as f:
    f.write('Результаты тестов:\n')  # Записываем заголовок файла

    for test_method in test_methods:
        print(f"Тест: {test_method} для pet_id '{run_tests.pet_id}' был запущен")
        f.write(f"Тест: {test_method} для pet_id '{run_tests.pet_id}' был запущен\n")

        try:
            getattr(run_tests, test_method)(run_tests.pet_id)
            print(f"Тест '{test_method}' PASS.")
            f.write(f"Тест '{test_method}' PASS.\n")
        except AssertionError as e:
            print(f"Тест '{test_method}' FAILED: {e}")
            f.write(f"Тест '{test_method}' FAILED: {e}\n")
        except Exception as e:
            print(f"Тест '{test_method}' ERROR: {e}")
            f.write(f"Тест '{test_method}' ERROR: {e}\n")

print(f"\nРезультаты тестов записаны в файл: {results_file}")




