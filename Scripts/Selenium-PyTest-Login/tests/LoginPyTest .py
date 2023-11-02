from pages.Login import *
from pages.MainPage import *

from selenium import webdriver
import time
import pytest

class LoginTests(pytest.m):
    @classmethod
    def setUpClass(cls) -> None:
        
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Log_in(self.driver)
        mainpage = Main_Page(self.driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()

        mainpage.check_main_page()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()