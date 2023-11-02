from Locators import *
class Main_Page:
    def __init__(self,driver):
        self.driver = driver
        
    def check_main_page (self):
        self.driver.find_element(*dashboard_lable_cssselector)   