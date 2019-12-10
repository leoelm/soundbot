import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SoundCloud():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.copy = 0
        self.links = []

    def open_soundcloud(self):
        self.driver.get('https://soundcloud.com/user-150334980/tracks')

    def get_songs(self):
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if (self.copy and 'user-150334980/' in elem.get_attribute("href") and (elem.get_attribute('href') not in self.links) and ('comments' not in elem.get_attribute('href')) and ('likes' not in elem.get_attribute('href')) and ('followers' not in elem.get_attribute('href')) and ('tracks#' not in elem.get_attribute('href')) and ('tracks' not in elem.get_attribute('href')) and ('following' not in elem.get_attribute('href'))):
                self.links.append(elem.get_attribute("href"))
            elif elem.get_attribute("href") == 'https://soundcloud.com/user-150334980/reposts':
                self.copy =1
        self.copy = 0
        return self.links

    def song_listen(self):
        for elem in self.links:
            self.driver.get(elem)
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[@class="sc-button-play playButton sc-button m-stretch"]').click()

            print('clicked')
            time.sleep(10)
            self.driver.close()
    def get_new(self):
        self.driver.get('https://soundcloud.com/user-150334980/always-gon-hate-young-tener')

    def listen_to_new(self):
            # self.driver.window_handles[i]
            # self.driver.switch_to.window(self.driver.window_handles[i])
        self.driver.refresh()
        try:
            check = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@class="sc-button-play playButton sc-button m-stretch"]')))
        except TimeoutException:
            self.driver.close()
            print('loading error')
            pass
        self.driver.find_element_by_xpath('//a[@class="sc-button-play playButton sc-button m-stretch"]').click()
        time.sleep(15)
            


if __name__ == '__main__':
    cloud = SoundCloud()
    cloud.get_new()
    # cloud.open_soundcloud()
    # cloud.get_songs()
    for i in range(1000):
        cloud.listen_to_new()
        print(i+1)



    