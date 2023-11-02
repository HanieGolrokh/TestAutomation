from playwright.sync_api import sync_playwright

def main():
    # Create a Playwright instance and launch a browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create a new page
        page = browser.new_page()

        # Navigate to a website
        page.goto('https://example.com')

        # Take a screenshot and save it to a file
        page.screenshot(path='example.png')

        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()
