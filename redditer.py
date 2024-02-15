from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json

def prepare_reddit(browser: webdriver.Firefox, scrollDownCount: int):
    for i in range(0, scrollDownCount):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
    
def get_links(browser: webdriver.Firefox):
    imgs = browser.find_elements(By.XPATH, value='//img[contains(@alt, "r/programmingmemes")]')
    for img in imgs:
        yield [i.strip() for i in img.get_attribute("srcset").split(",")]

def to_link_dictionary(links: list[str]):
    res = {}
    for link in links:
        split = link.split(" ")
        if (len(split) == 1):
            res[1] = split[0]
            break
        key = int(split[1].replace("w", "").strip())
        res[key] = split[0]
    return res 

def main():
    url = "https://www.reddit.com/r/programmingmemes/?rdt=42097"
    browser = webdriver.Firefox(options=Options())
    browser.get(url)
        
    prepare_reddit(browser, 20)

    linkCollection = [to_link_dictionary(i) for i in get_links(browser)]

    with open("res.json", "w") as fobj:
        json.dump(linkCollection, fobj)

if __name__ == "__main__":
    main()