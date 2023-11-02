from Login import *
from MainPage import *

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(3)

login = Log_in(driver)
mainpage = Main_Page(driver)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_on_login_button()

mainpage.check_main_page()

time.sleep(3)

print ("passed")