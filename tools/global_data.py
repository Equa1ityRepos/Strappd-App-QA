import os

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support.wait import *

# Constant Globals

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class FilterBar:
    food = MobileBy.ACCESSIBILITY_ID, 'Food'
    shelter = MobileBy.ACCESSIBILITY_ID, 'Shelter'
    health = MobileBy.ACCESSIBILITY_ID, 'Health'
    resources = MobileBy.ACCESSIBILITY_ID, 'Resources'
    work = MobileBy.ACCESSIBILITY_ID, 'Work'


class Sort:
    bar = By.XPATH, '//android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.widget.ListView'
    cloths = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    hygiene = By.XPATH, '//android.widget.ListView/android.view.View[2]/android.view.View'
    resources_all = By.XPATH, '//android.widget.ListView/android.view.View[3]/android.view.View'
    transit = By.XPATH, '//android.widget.ListView/android.view.View[4]/android.view.View'
    assistance = By.XPATH, '//android.widget.ListView/android.view.View[5]/android.view.View'
    card1_amenities = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[3]'


class AcceptTerms:
    title = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]'
    text_agree_button = By.XPATH, '//*[contains(@text, "{}")]'.format('I Agree')
    text_cancel_button = By.XPATH, '//*[contains(@text, "{}")]'.format('Cancel')
    loading = By.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View'


class Header:
    menu = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.widget.Button'
    location_button = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]'
    title = By.XPATH, 'android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]'
    search = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
    phone = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View'
