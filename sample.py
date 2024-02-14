from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# https://realpython.com/modern-web-automation-with-python-and-selenium/

# Path to your WebDriver executable. Download from https://selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference

# URL for WhatsApp Web
url = 'https://web.whatsapp.com/'

opts = Options()
# Initialize Chrome WebDriver
browser = webdriver.Firefox(options=opts)
browser.get(url)

# Wait for the user to scan the QR code and log in
input("Press Enter after scanning QR code and logging in...")

# Find the search input field
while True:
    try:
        search_box = browser.find_element(by=By.XPATH, value='//div[contains(@title, "Sucheingabefeld")]')

        # Type the name of the contact or group you want to send the message to
        contact_name = "Eren"  # Change this to the name of your contact or group
        for e in contact_name:
            search_box.send_keys(e)

        search_box.send_keys(Keys.ENTER)
        # Wait for a while to ensure the chat window is fully loaded
        time.sleep(1)

        # Find the input field for typing the message
        input_box = browser.find_element(by=By.XPATH, value='//div[contains(@title, "Gib eine Nachricht ein.")]')
        
        # Type the message you want to send
        message = "Hello, World!"

        for m in message:
            input_box.send_keys(m)
        input_box.send_keys(Keys.ENTER)
        
    except KeyboardInterrupt:
        break
    except:
        continue


    # Wait for a while to ensure the message is sent
time.sleep(2)

    # Close the browser window
browser.quit()