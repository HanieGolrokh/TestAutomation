from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import json

# Read the JSON configuration file
with open('D:\Hanie\MySrc\TestAutomation\Scripts\Calculator\config.json', 'r') as file:
    config_data = json.load(file)

# Access URLs from the config data
website_url = config_data['website_url']


#create def for enter number
def enter_number(driver,x):
    x_str=str (x)
    for ch in x_str:
        click_number(driver,ch)

#create def for locating numbers
def click_number(driver,x):
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

#create def for enter operations
def enter_operation(driver,o):
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
def get_result(driver):
    display = driver.find_element(By.XPATH,'//*[@id="display"]')
    return display.text 

# Create an instance of the Chrome driver (you need to specify the path to your ChromeDriver executable)
driver = webdriver.Chrome()
# Open a website
driver.get(website_url)

# Read and execute test cases from the CSV file
with open('TestAutomation/Scripts/Calculator/TestData/calculator_test_data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for index,row in enumerate(csv_reader):

        enter_number(driver,row['x1'])

        enter_operation(driver,row['Operator'])

        enter_number(driver,row['x2'])
        
        enter_operation(driver,"=")

        display = get_result(driver)

        # Get the result and assert it
        assert display == row['Expected_Result'], f"Test failed row {index}: {row['x1']} {row['Operator']} {row['x2']} != {row['Expected_Result']}"

        enter_operation(driver,"C")
              
# Close the browser
driver.quit()


