import os

import self
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.support.wait import *

# Constant Globals
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
SEARCH_CHARLE = 'First Step House of Orange County'


class ResourceCards:
    card_1_front_page = By.XPATH, '//android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]'
    card_header_1 = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[1]'
    card_2_front_page = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]'
    card_header_2 = By.XPATH, '//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[1]'
    card_1_phone = By.XPATH, '//android.view.View[@content-desc="(410) 889-3001"]/android.widget.TextView'
    phone_manna= MobileBy.ID, 'com.android.dialer:id/dialpad_floating_action_button'
    email_manna= By.XPATH, '//android.view.View[@content-desc="saleem@mannahouseinc.org"]'
    website= By.XPATH, '//android.view.View[3]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View'
    facebook = By.XPATH, '//android.view.View[3]/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View'
    SVDP_logo = By.XPATH, '//android.view.View[@content-desc="St. Vincent de Paul of Baltimore logo"]'
    map_full_screen = By.XPATH, '//android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.widget.Button'

class Location:
    # location icon first page
    location_button = By. XPATH, '//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]'
    #location bar with current location text
    location_add_button = By. XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View'
    #location bar to add text
    location_add_text = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText'
    location_returned_1 = By.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]'
    location_clear_x = By.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]'
    location_current_location = By.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]'
    #to select the city typed into serach bar
    location_city_selector = By.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[4]/android.view.View'
    location_distance_1 =By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[8]/android.view.View'
    location_distance_2 = By.XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[8]/android.view.View'
    location_distance_3 = By.XPATH, '//android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[8]/android.view.View'

class Demographics:
    men = By.XPATH, '//android.view.View/android.view.View[2]/android.widget.Button[1]'
    men_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    men_page_2 = By.XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    men_page_3 = By.XPATH, '//android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    women = By.XPATH, '//android.view.View[2]/android.widget.Button[2]'
    woman_page_1= By. XPATH,'//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    women_page_2=By. XPATH,'//android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    women_page_3=By. XPATH,'//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    youth = By.XPATH, '//android.view.View/android.view.View[2]/android.widget.Button[3]'
    youth_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    youth_page_2 = By. XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    youth_page_3 = By. XPATH, '//android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    all = By.XPATH, '//android.view.View/android.view.View[2]/android.widget.Button[4]'
    all_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    all_page_2 = By.XPATH,'//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    all_page_3 = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    seniors = By.XPATH, '//android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button[1]'
    seniors_page_1 = By.XPATH, '//android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    seniors_page_2 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    seniors_page_3 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    disabled = By.XPATH, '//android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button[2]'
    disabled_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    disabled_page_2 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    disabled_page_3 = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    families = By. XPATH, '//android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button[3]'
    families_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    families_page_2 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    families_page_3 = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    lgbtq = By. XPATH, '//android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button[4]'
    lgbtq_page_1 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    lgbtq_page_2 = By.XPATH, '//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'
    lgbtq_page_3 = By.XPATH, '//android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[5]/android.view.View'



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
    back_arrow = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]'
    menu = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.widget.Button'
    location_button = By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]'
    title = By.XPATH, 'android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]'
    search = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
    phone = By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View'
