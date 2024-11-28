from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.gostteam.constants import VISIBILITY_ELEMENT_TIMEOUT_10_SEC
from lib.gostteam.elements.main_page_elements import MainPageElements

class GostTeamPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://gost.team/'
        self.__driver = driver
        self.__elements = MainPageElements(driver=self.__driver)

    @property
    def page_elements(self):
        return self.__elements

    def _wait_to_load(self, element):
        WebDriverWait(driver=self.__driver, timeout=VISIBILITY_ELEMENT_TIMEOUT_10_SEC).until(
            EC.visibility_of_element_located(
                (By.XPATH, element),
            )
        )

    def open_main_page(self):
        self.__driver.get(url=self.url)
        self._wait_to_load(
            element='//div[contains(text(), "Тестируем")]'
        )
        # Ищем элемент
        element = self.__driver.find_element(By.XPATH, '//div[contains(text(), "Тестируем")]')
        return element

    def main_page_text_element_styles(self):
        self._wait_to_load(
            element='//*[@id="recorddiv779656132"]/div[3]/div/div/div/div/div/h1/div'
        )
        # Ищем элемент
        text_element = self.__driver.find_element(By.XPATH, '//*[@id="recorddiv779656132"]/div[3]/div/div/div/div/div/h1/div')
        # Получаем цвет
        color = text_element.value_of_css_property('color')
        # Проверяем цвет
        expected_color = 'rgba(255, 255, 255, 1)' # Цвет в rgba-формате
        assert color == expected_color, f'Expected color {expected_color}, but got {color}.'

    def open_tests_form_page(self):
        self.__driver.get(url=f'{self.url}/orders')

    def switch_to_eng(self):
        self.page_elements.link_to_eng_version_main_page.click()

    def styles(self):
        self._wait_to_load(
            element='//div[contains(text(), "Тестируем")]'
        )
        # Ищем элемент
        text_element = self.__driver.find_element(By.XPATH, '//div[contains(text(), "Тестируем")]')
        # Получаем цвет
        color = text_element.value_of_css_property('color')
        # Проверяем цвет
        expected_color = 'rgba(255, 255, 255, 1)'  # Замените на ожидаемый цвет в формате rgba
        assert color == expected_color, f'Expected color {expected_color}, but got {color}.'

    def masks(self):
        self._wait_to_load(
            element='//*[@id="rec710819711"]/div/div[1]'
        )
        # Получаем элемент
        element = self.__driver.find_element(By.XPATH, '//*[@id="rec710819711"]/div/div[1]')
        # Возвращаем элемент
        return element

    def sent_button_rus(self):
        self._wait_to_load(
            element='//*[@id="form710819711"]/div[2]/div[7]/button'
        )
        # Получаем элемент
        element = self.__driver.find_element(By.XPATH, '//*[@id="form710819711"]/div[2]/div[7]/button')
        # Возвращаем элемент
        return element

    def sent_button_eng(self):
        self._wait_to_load(
            element='//*[@id="form625322355"]/div[2]/div[7]/button'
        )
        # Получаем элемент
        element = self.__driver.find_element(By.XPATH, '//*[@id="form625322355"]/div[2]/div[7]/button')
        # Возвращаем элемент
        return element

class GostTeamPageWithBlog:
    def __init__(self, driver: WebDriver):
        self.url = 'http://gostblog.desol.one/'
        self.__driver = driver
        self.__elements = MainPageElements(driver=self.__driver)

    @property
    def page_elements(self):
        return self.__elements

    def _wait_to_load(self, element):
        WebDriverWait(driver=self.__driver, timeout=VISIBILITY_ELEMENT_TIMEOUT_10_SEC).until(
            EC.visibility_of_element_located(
                (By.XPATH, element),
            )
        )

    def open_blog_page(self):
        self.__driver.get(url=f'{self.url}/blog/')
        self._wait_to_load(
            element='//*[@id="wp--skip-link--target"]/div[1]/h1'
        )
        element = self.__driver.find_element(By.XPATH, '//*[@id="wp--skip-link--target"]/div[1]/h1')
        return element

    def mail_field(self):
        self.__driver.get(url=f'{self.url}/blog/')
        self._wait_to_load(
            element='//*[@id="form_email_1"]'
        )
        element = self.__driver.find_element(By.XPATH, '//*[@id="form_email_1"]')
        # Возвращаем элемент
        return element
