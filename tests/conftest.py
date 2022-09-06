import webbrowser
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    return driver




