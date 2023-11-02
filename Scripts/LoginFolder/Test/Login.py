from Locators import *
class Log_in:
    def __init__(self, driver):
        self.driver = driver
        
    def enter_username(self,username):
        self.driver.find_element(*username_text_xpath).send_keys(username)
    def enter_password(self,password):    
        self.driver.find_element(*password_text_xpath).send_keys(password)
    def click_on_login_button(self):    
        self.driver.find_element(*login_button_xpath).click()    