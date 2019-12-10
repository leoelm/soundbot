import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class SoundCloud():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = 'https://soundcloud.com/user-150334980/tracks'
        self.actions = ActionChains(self.driver)

    def open_soundcloud(self):
        self.driver.get(self.link)
        try:
            check = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@class="sc-button-play playButton sc-button m-stretch"]')))
        except TimeoutException:
            pass

        main_window = self.driver.current_window_handle
        self.actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
        self.actions.reset_actions()

if __name__ == "__main__":
    s = SoundCloud()
    s.open_soundcloud()

    