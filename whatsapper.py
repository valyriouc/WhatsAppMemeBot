from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
import pyperclip3 as clip

class Whatsapper(webdriver.Firefox):
    def __init__(self, contacts: list[str], memes: list[str]) -> None:
        super().__init__(Options(), None, True)
        self.contacts = contacts
        self.memes = memes
        self.get("https://web.whatsapp.com/")

    def _search_for(self, contact):
        search_box = self.find_element(by=By.XPATH, value='//div[contains(@title, "Sucheingabefeld")]')
        clip.copy(contact)
        search_box.send_keys(Keys.CONTROL+"v")
        search_box.send_keys(Keys.ENTER)
     
    def _typing_in(self):
        input_box = self.find_element(by=By.XPATH, value='//div[contains(@title, "Gib eine Nachricht ein.")]')
        for meme in self.memes:
            clip.copy(meme)
            input_box.send_keys(Keys.CONTROL + "v")
            input_box.send_keys(Keys.ENTER)
    
    def send(self):
        input("Press Enter after scanning the QR code...")
        for contact in self.contacts:
            self._search_for(contact)
            self._typing_in()

def main():
    memes = None
    with open("memes.json", "r") as fobj:
        memes = json.load(fobj)

    browser = Whatsapper(["Ich"], memes)
    browser.send()
    browser.quit()

    print("Bot is done sending the memes!")
        
if __name__ == "__main__":
    main()