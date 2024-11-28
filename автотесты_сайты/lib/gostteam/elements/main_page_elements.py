from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPageElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def header(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[contains(@class, "imglogo")]/ancestor::div[contains(@class, "maincontainer")]',
        )

    @property
    def link_to_eng_version_main_page(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[contains(@class, "langs_lang")]/a[contains(text(), "En")]'
        )