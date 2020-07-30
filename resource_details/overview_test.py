import unittest
from appium import webdriver
from tools.ex_conds import *
from appium.webdriver.common.touch_action import TouchAction
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'deviceName': 'Android',
            'app': PATH('..\\tools\\app\\org.strappd.apk'),
            "appPackage": "org.strappd",
            "appActivity": ".MainActivity",
            "ignoreUnimportantViews": "true",
            "autoGrantPermissions": "true",
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_0a_skip_onboarding(self):
        get_through_onboarding(self)

    def test_0b_get_charle(self):
        # Select a Resource Card from list
        search_by_text_and_click(self, SEARCH_CHARLE)

    def test_1a_details_page_title(self):
        # user is navigated to Resource Details page
        # Card Displayed Title
        element_visible(self, CardDetails.title)

    def test_1b_details_page_title_with_text(self):
        # Title match what was selected on main page
        element_has_text(self, CardDetails.title, SEARCH_CHARLE)

    def test_2a_amenities(self):
        # Card Lists Amenities
        element_has_text(self, CardDetails.amenities, "Sober Living")

    def test_3a_contact(self):
        # Contact Information is displayed
        # Phone, Email, Webpage, Social Media Link
        p = get_text_from_element(self, CardDetails.charle_phone)
        print(p)
        element_has_text(self, CardDetails.charle_phone, '(949) 642-2941')
        element_has_text(self, CardDetails.charle_email, 'info@charlestreet.org')
        element_has_text(self, CardDetails.web_page, 'http://www.charlestreet.org')
        element_has_text(self, CardDetails.social_media1, 'https://www.facebook.com/FirstStepHouseofOC/')

    def test_3b_address(self):
        # Address is displayed
        element_has_text(self, CardDetails.address, '2015 Charle St, Costa Mesa, CA 92828')

    def test_3c_map(self):
        # A maps view is displayed
        visible_assert(self, CardDetails.map)

    def test_3d_map_pub_tansit(self):
        # route is defauled by public transportation
        scroll_down(self)
        print('Dont sure How to do this step')

    def test_4_hours(self):
        # Bottom of card
        # Weekly hours are displayed and demographics
        element_has_text(self, CardDetails.contact_text, 'Please contact this service for hours')


if __name__ == '__main__':
    unittest.main()
