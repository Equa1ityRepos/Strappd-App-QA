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
    search = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
    phone = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View'

class Options:
    menu_drawer_back = By.XPATH, '//android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.widget.Button'
    menu_back = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]'
    map_view = By.XPATH, '//android.view.View[4]/android.view.View[1]/android.widget.TextView'
    crisis_lines = By.XPATH, '//android.view.View[@content-desc="Crisis Lines"]/android.widget.TextView'
    my_favorites = By.XPATH, '//android.view.View[@content-desc="My Favorites"]/android.widget.TextView'
    about_strappd = By.XPATH, '//android.view.View[@content-desc="About STRAPPD"]/android.widget.TextView'
    show_tutorial = By.XPATH, '//android.view.View[@content-desc="Show Tutorial"]/android.widget.TextView'
    give_feedback = By.XPATH, '//android.view.View[@content-desc="Give Feedback"]'
    terms_and_privacy = By.XPATH, '//android.view.View[10]/android.view.View[3]'
    provider_login = By.XPATH, '//android.view.View[@content-desc="Provider Login / SignUp"]/android.widget.TextView'
    back_arrow_crisis = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]'
    back_arrow_about = By.XPATH, '//android.view.View[1]/android.view.View[1]/android.view.View/android.widget.Button'
    cancel_button_provider_login = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.widget.Button'
    back_arrow_give_feedback = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]'
    back_arrow_terms_and_privacy = By.XPATH, '//android.view.View[1]/android.view.View[1]/android.view.View/android.widget.Button'
    back_button_provider_cancel = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button'
    crisis_lines_header = By.XPATH, '//android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]'
    feedback_email_field = By.XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText'
    feedback_subject_field = By.XPATH, '//android.view.View/android.view.View/android.view.View[2]/android.widget.EditText'
    feedback_message_field = By.XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText'
    feedback_send_button = By.XPATH, '//android.view.View[@content-desc="Send Feedback"]'
