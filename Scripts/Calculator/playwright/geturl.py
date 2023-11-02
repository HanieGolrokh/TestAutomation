from playwright.sync_api import sync_playwright
import json

# Read the configuration from the JSON file
with open('D:\Hanie\MySrc\TestAutomation\Scripts\Calculator\playwright\config.json', 'r') as config_file:
    config = json.load(config_file)
# Get the URL from the configuration
url = config.get('url')

print('URL from config:', url)    

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    current_url = page.url
    print('Current URL:', current_url)






