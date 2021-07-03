from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import uniform
from secrets import username, password
import json

cck_blockers = json.loads(open('CckBlocker.json').read())
attribute_list = []

class TinderBot():
    driver = webdriver.Chrome()
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        login_btn = self.driver.find_element_by_xpath('// *[ @ id = "u2005023502"] / div / div[1] / div / main / div[1] / div / div / div / div / header / div / div[2] / div[2] / a / span')
        login_btn.click()

        sleep(1)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        pw_in.send_keys(Keys.ENTER)
        self.driver.switch_to_window(base_window)

        sleep(7)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[1]/span')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div/div/div[3]/button[2]/span')
        popup_2.click()

        cookies = self.driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[2]/div/div/div[1]/button')
        cookies.click()

        sleep(4)

    def like(self):
        like = r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]'
        swipe_right = self.driver.find_element_by_xpath(like)
        swipe_right.click()

    def subs_like (self):
        subs_like=r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]'
        subs_like_btn = self.driver.find_element_by_xpath(subs_like)
        subs_like_btn.click()

    def vaccinated_like(self):
        #this function to deal with exceptions thrown by profiles with "Vaccinated" badge
        vaccinated_like = r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'
        vaccinated_like_btn= self.driver.find_element_by_xpath(vaccinated_like)
        vaccinated_like_btn.click()

    def dislike(self):
        dislike = r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button'
        dislike_btn = self.driver.find_element_by_xpath(dislike)
        dislike_btn.click()


    def close_popup(self):
        popup_3= r'//*[@id="u276642426"]/div/div/div[3]/button'
        popup_3 = self.driver.find_element_by_xpath(popup_3)
        popup_3.click()


    def close_match(self):
        close_match= r'//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button'
        match_popup = self.driver.find_element_by_xpath(close_match)
        match_popup.click()


    def selector (self):
        sleep(3)
        Name = r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div/span'
        description= r'//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div'
        name_get=self.driver.find_element_by_xpath(Name).text
        print(name_get)
        attribute_list= self.driver.find_element_by_xpath(description).text.split(" ")
        print(attribute_list)
        test= any(x in attribute_list for x in cck_blockers)
        if test is True:
            self.dislike()
        else:
            self.subs_like()

    def auto_swipe(self):
        while True:
            try:
                sleep(uniform(2, 3))
                self.selector()
            except Exception:
                try:
                    sleep(2.12)
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        try:
                            sleep(0.5)
                            self.close_match()
                        except Exception:
                            try:
                                self.vaccinated_like()
                            except Exception:
                                    self.subs_like()






run = TinderBot()
run.login()
run.auto_swipe()