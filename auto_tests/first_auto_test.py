# Простенький автотест на рандомном сайте (который теперь не падает)

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.kubsu.ru/user')
    driver.find_element(By.ID, 'edit-name').send_keys('user1@gosy.com')
    driver.find_element(By.ID, 'edit-pass').send_keys('34234234rfwe43')
    driver.find_element(By.ID, 'edit-submit').click()
    error_text = driver.find_element(By. CSS_SELECTOR, '[class="messages error"]').text
    assert ('Извините, это имя пользователя или пароль неверны. ' in error_text)




