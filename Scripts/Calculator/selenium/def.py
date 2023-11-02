from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Create an instance of the Chrome driver (specify the path to your ChromeDriver executable)
driver = webdriver.Chrome()

# Open a website
driver.get('file:///D:/Hanie/Source/Front/Calculator/page.html')

# Function to perform calculator operations based on test data
def perform_calculation(test_data):
    number1, operator, number2, expected_result = test_data

    # Enter Number1
    enter_number(float(number1))

    # Enter Operator
    enter_operation(operator)

    # Enter Number2
    enter_number(float(number2))

    # Perform calculation
    enter_operation("=")

    # Get the result and assert it
    display = get_result()
    assert float(display) == float(expected_result), f"Test failed: {number1} {operator} {number2} != {expected_result}"

# Function to enter a number
def enter_number(x):
    x_str = str(x)
    for ch in x_str:
        click_number(ch)

# Function to click calculator buttons for numbers
def click_number(x):
    num = driver.find_element(By.XPATH, f'/html/body/div/div[2]/button[contains(text(), "{x}")]')
    num.click()

# Function to enter an operation
def enter_operation(o):
    operation = driver.find_element(By.XPATH, f'/html/body/div/div[2]/button[contains(text(), "{o}")]')
    operation.click()

# Function to get the result
def get_result():
    display = driver.find_element(By.XPATH, '//*[@id="display"]')
    return display.text

# Read and execute test cases from the CSV file
with open('D:/Hanie/Source/TestData/Calculator/calculator_test_data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        perform_calculation([row['Number1'], row['Operator'], row['Number2'], row['Expected_Result']])

# Close the browser
driver.quit()
