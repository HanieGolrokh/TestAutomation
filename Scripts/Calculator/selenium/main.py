from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Import the time module
import csv

# Create an instance of the Chrome driver (you need to specify the path to your ChromeDriver executable)
driver = webdriver.Chrome()

#create def for enter number
def enter_number(x):
    x_str=str (x)
    for ch in x_str:
        click_number(ch)


def click_number(x):
    if x == "0":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[14]")
    
    elif x == "1":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[10]")
        
    elif x == "2":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[11]")

    elif x == "3":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[12]")

    elif x == "4":    
        num = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[6]')
    
    elif x == "5":    
        num = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[7]')
    
    elif x == "6":    
        num = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[8]')

    elif x == "7":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[2]")
    
    elif x == "8":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[3]")
       
    elif x == "9":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[4]")
        
    elif x == ".":
        num = driver.find_element(By.XPATH, "/html/body/div/div[2]/button[15]")
    num.click() #0

#create def for enter operation
def enter_operation(o):
     if o == "C":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[1]')

     elif o == "+":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[5]')

     elif o == "-":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[9]')

     elif o == "*":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[13]')

     elif o == "/":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[17]')
    
     elif o == "=":
        operation = driver.find_element(By.XPATH,'/html/body/div/div[2]/button[16]')
    
     operation.click()

#create def for get result
def get_result():
    display = driver.find_element(By.XPATH,'//*[@id="display"]')
    return(display.text) #5


# Open a website
driver.get('file:///D:/Hanie/Source/Front/Calculator/page.html')

enter_number(.96)

enter_operation("-")

enter_number(.41)

enter_operation("=")

display = get_result()

# Get the result and assert it
assert display == '0.55'

# Close the browser
driver.quit()


