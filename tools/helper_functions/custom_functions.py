import os
import unittest
import re
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import *
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from tools.global_data import *
from tools.ex_conds import *
import random
import string
from tools.ex_conds import *
from tools.helper_functions.filters_helpers import filter_helpers_amenities_list



def compare_card_1(self,locator1, locator2):
    card_1 = get_text_from_element(self, locator1)
    print(card_1)
    element_click(self, ResourceCards.card_1_front_page)
    element_invisible(self,AcceptTerms.loading)
    nameOnCard = get_text_from_element(self,locator2)
    print(nameOnCard)
    if card_1 == nameOnCard:
        return True
    else:
        print("they are not the same")

def compare_card_2(self,locator1, locator2):
    card_1 = get_text_from_element(self, locator1)
    element_click(self, ResourceCards.card_2_front_page)
    element_invisible(self,AcceptTerms.loading)
    nameOnCard = get_text_from_element(self,locator2)
    if card_1 == nameOnCard:
        return True
    else:
        print("they are not the same")



def check_distance(self, locator, less_than_number):
    string = get_text_from_element(self, locator)
    split_text = string.split(' ')
    print(split_text)
    number = []
    number.append(split_text[0])
    strings = [str(integer) for integer in number]
    a_string = "".join(strings)
    a_float = float(a_string)
    if a_float < less_than_number:
        return True
    else:
        return False



def check_text(self, locator, text):
    check = get_text_from_element(self,locator)
    if text in check:
        return True
    else:
        print(text + " not found in " + check)


def click_menu(self):
    element_click(self, Header.menu)

def get_through_onboarding(self):
    sleep(10)
    element_click(self, AcceptTerms.skip)
    sleep(5)
    element_click(self, AcceptTerms.text_agree_button)
    element_invisible(self, AcceptTerms.loading)
    element_visible(self, Header.menu)



def click_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).click()


def find_by_text(self, text):
    self.driver.implicitly_wait(1)
    try:
        self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).is_displayed()
        print('Element is displayed')
        return True
    except Exception as r:
        print('Element is not displayed')
        return False


def search_by_text_and_click(self, text):
    sleep(2)
    element = self.driver.find_elements_by_class_name('android.widget.Button')
    print(element)
    search = element[1]
    search.click()
    element_send_text(self, search_charle.field, text)
    element_invisible(self, AcceptTerms.loading)
    element_has_text(self, CardDetails.dash_card1_title, text)
    element_click(self, CardDetails.dash_card1_title)


def visible_assert(self, element):
    self.driver.implicitly_wait(30)
    try:
        self.driver.find_element(element)
        print('Element is displayed')
        return True
    except NoSuchElementException as e:
        print('Element is not displayed')
        return False
    self.driver.implicitly_wait(20)


def standard_search(self, search_text, list_text):
    self.driver.implicitly_wait(20)
    element_send_text(self, AcceptTerms.skip, 20)
    reddit_list = search_cards(self)
    print(reddit_list)
    self.assertTrue(search_any_text_in_list(list_text, reddit_list))


def search_cards(self):
    self.driver.implicitly_wait(5000)
    search_list = []
    row1xpath = '//android.widget.RelativeLayout['
    xpathend = ']/android.widget.TextView[1]'
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path1)) > 0:
            self.driver.implicitly_wait(1)
            search_list.append(self.driver.find_element_by_xpath(f"{row1xpath}{index}{xpathend}").text)
        else:
            break
    return search_list


def scroll_down(self):
    screen = self.driver.get_window_size()
    x = screen['width']
    y = screen['height']
    self.driver.swipe(start_x=x / 2, start_y=y * 3 / 4, end_x=x / 2, end_y=y / 3, duration=800)


def scroll_up(self):
    screen = self.driver.get_window_size()
    x = screen['width']
    y = screen['height']
    self.driver.swipe(start_x=x / 2, start_y=y / 2, end_x=x / 2, end_y=y / 100 * 90, duration=800)


def get_random_letters(self):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_string = []
    random_string = ''.join(random.choice(letters) for i in range(2))
    return random_string


def search_any_text_in_list(text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False


def amenities_check(self, element):
    text = get_text_from_element(self, element)
    element_click(self, element)
    element_invisible(self, AcceptTerms.loading)
    amenities_string = get_text_from_element(self, Sort.card1_amenities)
    card_list = [x for x in re.split(',| ', amenities_string) if x != '']
    print(text)
    amenities_key = filter_helpers_amenities_list(text)
    self.assertTrue(any(amenity in card_list for amenity in amenities_key), f"\nDid not find a match from\n{amenities_key}\nin\n{card_list}")
