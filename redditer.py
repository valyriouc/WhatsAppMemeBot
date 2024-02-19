from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json
import os 

class Redditer(webdriver.Firefox):
    def __init__(self, subreddit: str, scrollCount: int) -> None:
        super().__init__(Options(), None, True)
        self.get(f"https://www.reddit.com/r/{subreddit}/")
        self.scrollCount = scrollCount

    def _prepare_reddit(self):
        for _ in range(0, self.scrollCount):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(0.5)
    
    def _get_links(self):
        imgs = browser.find_elements(By.XPATH, value='//img[contains(@alt, "r/programmingmemes")]')
        for img in imgs:
            yield [i.strip() for i in img.get_attribute("srcset").split(",")]
    
    @staticmethod
    def _get_highest_link(links: list[str]) -> str:
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
    
    def render(self):
        self._prepare_reddit()
        return [Redditer._get_highest_link(i) for i in self._get_links()]

def main(renderer: Redditer, storefile: str):
    oldCollection = []
    if (os.path.exists(storefile)):
        with open(storefile, "r") as fobj:
            oldCollection = list(json.load(fobj))
    linkCollection = [d for d in renderer.render() if d not in oldCollection and d != ""] 
    oldCollection.extend(linkCollection)
    with open(storefile, "w") as fobj:
        json.dump(oldCollection, fobj)

if __name__ == "__main__":
    browser = Redditer("programmingmemes", 20)
    main(browser, "memes.json")
    browser.quit()