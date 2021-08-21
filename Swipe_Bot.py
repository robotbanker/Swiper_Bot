import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import uniform
from secrets import username, password
from os import rename
from datetime import datetime
import json

cck_blockers = json.loads(open('CckBlocker.json').read())
attribute_list = []
bot_results = {
    'Name': [],
    'Vote': [],
    'Triggers': [],
    'Description': [],
}

now = datetime.now()
date_time = now.strftime("%m-%d-%Y_%H%M%S")


class TinderBot():
    driver = webdriver.Chrome()

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        login_btn = self.driver.find_elements_by_xpath("//*[contains(text(),'Log in')]")
        login_btn[0].click()
        sleep(1)
        fb_btn = self.driver.find_element_by_xpath("//*[contains(text(),'Login with Facebook')]")
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        # input email
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        # input password
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        pw_in.send_keys(Keys.ENTER)
        self.driver.switch_to.window(base_window)
        sleep(6)
        # close/accept popup:
        popup_1 = self.driver.find_elements_by_xpath("//*[contains(text(),'Allow')]")
        popup_1[0].click()
        sleep(2)
        popup_2 = self.driver.find_elements_by_xpath("//*[contains(text(),'Not interested')]")
        popup_2[0].click()
        cookies = self.driver.find_elements_by_xpath("//*[contains(text(),'I accept')]")
        cookies[0].click()
        sleep(4)

    def like(self):
        like = "//*[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)']"
        swipe_right = self.driver.find_element_by_xpath(like)
        swipe_right.click()

    def dislike(self):
        dislike = "//*[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-pink)']"
        dislike_btn = self.driver.find_element_by_xpath(dislike)
        dislike_btn.click()

    def close_popup(self):
        popup_3 = "//*[contains(text(),'Not interested')]"
        popup_3 = self.driver.find_element_by_xpath(popup_3)
        popup_3.click()

    def close_match(self):
        close_match = '//*[@aria-label="Close"]'
        match_popup = self.driver.find_element_by_xpath(close_match)
        match_popup.click()

    def selector(self):
        sleep(uniform(1, 2))
        Name = "//*[@itemprop='name']"
        description = "//*[@class='BreakWord Whs(pl) Fz($ms) Ta(start) Animn($anim-slide-in-left) Animdur($fast) LineClamp(5,118.125px)']"
        name_get = self.driver.find_element_by_xpath(Name).text
        text_descr = self.driver.find_element_by_xpath(description).text
        attribute_list = self.driver.find_element_by_xpath(description).text.split(" ")
        test = any(x in attribute_list for x in cck_blockers)
        trigger = set.intersection(set(attribute_list), set(cck_blockers))
        if test is True:
            self.dislike()
            verdict = 'swipe left'
        else:
            self.like()
            verdict = 'swipe right'
        bot_results['Name'].append(name_get)
        bot_results['Description'].append(text_descr + ' ')
        bot_results['Vote'].append(verdict)
        bot_results['Triggers'].append(trigger)
        print(name_get)
        print(verdict)
        print(trigger)
        print(text_descr)

    def auto_swipe(self):
        n = int(0)
        while True:
            n = n + 1
            k = 10
            print(n)
            data = pd.DataFrame.from_dict(bot_results, orient='index')
            df = data.transpose()
            if n % k == 0:
                df.to_csv(r'C:\Users\Davide Solla\PycharmProjects\SwipeBot\sink\Bot_Results.csv')
                # self.file_save()
            try:
                self.selector()
            except Exception:
                try:
                    sleep(2.12)
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        sleep(0.5)
                        self.close_match()

    def close(self):
        self.driver.quit()


run = TinderBot()

run.login()
try:
    run.auto_swipe()
except Exception:

    os.rename(r'C:\Users\Davide Solla\PycharmProjects\SwipeBot\sink\Bot_Results.csv',
              fr'C:\Users\Davide Solla\PycharmProjects\SwipeBot\sink\Bot_Results_as-of-{date_time}.csv')
    sleep(20)
    run2 = TinderBot()
    run2.login()
    run2.auto_swipe()
