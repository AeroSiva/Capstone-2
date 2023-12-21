from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from Data import data 
import pytest

@pytest.fixture(scope="class")
def setup(request):
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        wait = WebDriverWait(driver, 30)
        driver.maximize_window()
        driver.get(data.OrangeHrm_data2().login_url)
        request.cls.driver = driver
        request.cls.wait = wait
        yield
        driver.close()
    
    except Exception as e:
        print("Conftest setup error : ",e)