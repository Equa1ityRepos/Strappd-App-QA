import os

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support.wait import *

# Constant Globals
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
SEARCH_CHARLE = 'First Step House of Orange County'


class FilterBar:
    food = By.XPATH, '//android.view.View[@content-desc="Food"]/android.widget.TextView'
    shelter = By.XPATH, '//android.view.View[@content-desc="Shelter"]/android.widget.TextView'
    health = By.XPATH, '//android.view.View[@content-desc="Health"]/android.widget.TextView'
    resources = By.XPATH, '//android.view.View[@content-desc="Resources"]/android.widget.TextView'
    work = By.XPATH, '//android.view.View[@content-desc="Work"]/android.widget.TextView'


class Sort:
    bar = By.XPATH, '//android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.widget.ListView'
    cloths = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    hygiene = By.XPATH, '//android.widget.ListView/android.view.View[2]/android.view.View'
    resources_all = By.XPATH, '//android.widget.ListView/android.view.View[3]/android.view.View'
    transit = By.XPATH, '//android.widget.ListView/android.view.View[4]/android.view.View'
    assistance = By.XPATH, '//android.widget.ListView/android.view.View[5]/android.view.View'
    card1_amenities = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[3]'
    soup_kitchen = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    food_pantries = By.XPATH, "//android.widget.ListView/android.view.View[3]/android.view.View"
    all = By.XPATH, '//android.widget.ListView/android.view.View[2]/android.view.View'
    medical = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    counseling = By.XPATH, '//android.widget.ListView/android.view.View[3]/android.view.View'
    education = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    employment = By.XPATH, '//android.widget.ListView/android.view.View[3]/android.view.View'
    emergency = By.XPATH, '//android.widget.ListView/android.view.View[1]/android.view.View'
    transitional = By.XPATH, '//android.widget.ListView/android.view.View[3]/android.view.View'


class CardDetails:
    dash_card1_title = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]'
    title = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[1]'
    amenities = By.XPATH, '//android.view.View/android.view.View[2]/android.widget.TextView'
    charle_phone = By.XPATH, '//android.view.View[@content-desc="(949) 642-2941"]/android.widget.TextView'
    charle_email = By.XPATH, '//android.view.View[@content-desc="info@charlestreet.org"]/android.widget.TextView'
    web_page = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[2]/android.view.View'
    social_media1 = By.XPATH, '//android.view.View[4]/android.view.View/android.view.View[2]/android.view.View'
    social_media2 = By.XPATH, '//android.view.View[5]/android.view.View/android.view.View[2]/android.view.View'
    address = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]'
    map = By.XPATH, By.XPATH, '//android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.view.View[1]'
    contact_text = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]' # Please contact this service for hours

class search_charle:
    field = By.XPATH, '//android.widget.EditText'



class AcceptTerms:
    skip = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]'
    title = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]'
    text_agree_button = By.XPATH, '//*[contains(@text, "{}")]'.format('I Agree')
    text_cancel_button = By.XPATH, '//*[contains(@text, "{}")]'.format('Cancel')
    loading = By.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View'


class Header:
    menu = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.widget.Button'
    location_button = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]'
    title = By.XPATH, 'android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]'
    search = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
    phone = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View'
