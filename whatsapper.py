from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def main():
    url = "https://www.reddit.com/r/programmingmemes/?rdt=42097"
    browser = webdriver.Firefox(options=Options())
    browser.get(url)
    for i in range(0, 20):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

    imgs = browser.find_elements(By.XPATH, value='//img[contains(@alt, "r/programmingmemes")]')

    with open("testing.txt", "w") as fobj:
        for img in imgs:
            testing = img.get_attribute("srcset")
            fobj.write(testing + "\n")
    

if __name__ == "__main__":
    main()