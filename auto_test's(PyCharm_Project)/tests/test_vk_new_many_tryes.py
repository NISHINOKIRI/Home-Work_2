# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# RESULT_FILE = "test_results.txt"
#
#
# class VKLogin(unittest.TestCase):
#
#     def write_clea_file(sels):
#         with open(RESULT_FILE, "w", encoding="utf-8") as file:
#             file.write('')
#
#     @staticmethod
#     def write_result(result):
#         with open(RESULT_FILE, "a", encoding="utf-8") as file:
#             file.write(result)
#
#     def test_login_with_invalid_credentials(self):
#         for i in range(10):  # Выполняем тест 3 раза
#             with self.subTest(i=i):  # Каждый проход будет подгруппой
#                 driver = webdriver.Firefox()
#                 driver.implicitly_wait(0+i)
#                 try:
#                     driver.get('https://vk.com')
#                     driver.find_element(By.CSS_SELECTOR, '#index_email').send_keys('user1@gmail.com')
#                     driver.find_element(By.CSS_SELECTOR, 'button.FlatButton:nth-child(5) > span:nth-child(1)').click()
#                     time.sleep(0 + i)
#                     error_text = driver.find_element(By.CSS_SELECTOR, '.vkuiModalCardBase__container').text
#                     self.assertIn('Слишком много попыток. Попробуйте позже. [9]', error_text)
#                     result = f"Тест 'VK_invailid_many_tries' прошел успешно: Сообщение об ошибке найдено (попытка {i + 1}).\n"
#                     print(result)
#                     self.write_result(result)  # Записываем результат в файл
#                     break
#                 except AssertionError:
#                     result = f"Тест 'VK_invailid_many_tries' не прошел на попытке {i + 1}, см. AssertionError:\n"
#                     print(result)
#                     self.write_result(result)
#                     self.fail("сообщение не содержит заданный текст")  # Отчет о падении теста.
#                 except Exception as e:
#                     print(f"Произошла ошибка на попытке {i + 1}: {e}")
#                     self.fail("Произошла ошибка: " + str(e))  # Отчет о другой ошибке (если есть)
#                 finally:
#                     driver.quit()  # Закрытие браузера после теста
#
#     def test_login_random_web_site(self):
#         for i in range(10):  # Выполняем тест 3 раза
#             with self.subTest(i=i):  # Каждый проход будет подгруппой
#                 driver = webdriver.Chrome()
#                 driver.implicitly_wait(3)
#                 try:
#                     driver.get('https://www.kubsu.ru/user')
#                     driver.find_element(By.ID, 'edit-name').send_keys('user1@gosy.com')
#                     driver.find_element(By.ID, 'edit-pass').send_keys('34234234rfwe43')
#                     driver.find_element(By.ID, 'edit-submit').click()
#                     time.sleep(0 + i)
#                     error_text = driver.find_element(By.CSS_SELECTOR, '[class="messages error"]').text
#                     self.assertIn('Извините, это имя пользователя или пароль неверны. ', error_text)
#                     result = f"Тест 'Invailid_parameters_login_randon_web_site' прошел успешно: Сообщение об ошибке найдено (попытка {i + 1}).\n"
#                     print(result)
#                     self.write_result(result)  # Записываем результат в файл
#                     break
#                 except AssertionError:
#                     result = f"Тест 'Invailid_parameters_login_randon_web_site' не прошел на попытке {i + 1}, см. AssertionError:\n"
#                     print(result)
#                     self.fail("сообщение не содержит заданный текст")  # Отчет о падении теста.
#                 except Exception as e:
#                     print(f"Произошла ошибка: {e}")
#                     self.fail("Произошла ошибка: " + str(e))  # Отчет о другой ошибке (если есть)
#                 finally:
#                     driver.quit()  # Закрытие браузера после теста 2