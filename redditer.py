from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json
import os 

def prepare_reddit(browser: webdriver.Firefox, scrollDownCount: int):
    for _ in range(0, scrollDownCount):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
    
def get_links(browser: webdriver.Firefox):
    imgs = browser.find_elements(By.XPATH, value='//img[contains(@alt, "r/programmingmemes")]')
    for img in imgs:
        yield [i.strip() for i in img.get_attribute("srcset").split(",")]

def get_highest_link(links: list[str]) -> str:
    highest = -1
    link = ""
    for link in links:
        split = link.split(" ")
        if (len(split) == 1):
            continue
        key = int(split[1].replace("w", "").strip())
        if (key > highest):
            highest = key
            link = split[0]
    return link.split(" ")[0].strip()

def main(browser: webdriver.Firefox, subreddit: str, storefile: str):
    url = f"https://www.reddit.com/r/{subreddit}/"
    browser.get(url)

    prepare_reddit(browser, 20)

    oldCollection = []
    if (os.path.exists(storefile)):
        with open(storefile, "r") as fobj:
            oldCollection = list(json.load(fobj))

    linkCollection = [d for d in (get_highest_link(i) for i in get_links(browser)) if d not in oldCollection and d != ""] 

    for i in linkCollection:
        print(i)

    oldCollection.extend(linkCollection)

    with open(storefile, "w") as fobj:
        json.dump(oldCollection, fobj)

if __name__ == "__main__":
    browser = webdriver.Firefox(options=Options())
    main(browser, "programmingmemes", "memes.json")
    browser.quit()