from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json

def main(browser: webdriver.Firefox, contact: str):
    # URL for WhatsApp Web
    url = 'https://web.whatsapp.com/'

    browser.get(url)

    # Wait for the user to scan the QR code and log in
    input("Press Enter after scanning QR code and logging in...")

    # Find the search input field
    while True:
        try:
            search_box = browser.find_element(by=By.XPATH, value='//div[contains(@title, "Sucheingabefeld")]')

            contact_name = contact 
            for e in contact_name:
                search_box.send_keys(e)

            search_box.send_keys(Keys.ENTER)

            time.sleep(1)

            input_box = browser.find_element(by=By.XPATH, value='//div[contains(@title, "Gib eine Nachricht ein.")]')

            memes = None
            with open("memes.json", "r") as fobj:
                memes = json.load(fobj)

            for meme in memes:
                for m in meme:
                    input_box.send_keys(m)
                input_box.send_keys(Keys.ENTER)
            time.sleep(1)
        
        except KeyboardInterrupt:
            print("Bot is shutting down!")
            break
        except:
            continue

if __name__ == "__main__":
    browser = webdriver.Firefox(Options())
    main(browser, "Ich")
    browser.quit()