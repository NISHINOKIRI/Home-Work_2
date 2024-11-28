import pytest
from selenium import webdriver
from lib.gostteam.page.gostteam_page import GostTeamPage
from lib.gostteam.page.gostteam_page import GostTeamPageWithBlog

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def gost_team_page(browser: webdriver) -> GostTeamPage:
    return GostTeamPage(driver=browser)

@pytest.fixture
def gost_team_page_with_blog(browser: webdriver) -> GostTeamPageWithBlog:
    return GostTeamPageWithBlog(driver=browser)
