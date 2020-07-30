import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep
import time
import re


class LocationTestCases(unittest.TestCase):

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

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)

    def test_1_current(self):
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Location.location_button)
        element_invisible(self, AcceptTerms.loading)
        #searching by current location
        element_click(self, Location.location_current_location)
        element_invisible(self, AcceptTerms.loading)
        self.assertTrue(check_distance(self, Location.location_distance_1, 10))
        self.assertTrue(check_distance(self, Location.location_distance_2, 10))
        self.assertTrue(check_distance(self, Location.location_distance_3, 10))



    def test_2_SLC(self):
        element_invisible(self, AcceptTerms.loading)
        # click on location_icon
        element_click(self, Location.location_button)
        #add text to navigation bar
        element_click(self, Location.location_add_text )
        element_send_text(self, Location.location_add_text, 'Salt Lake City')
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Location.location_city_selector)
        self.assertTrue(check_distance(self, Location.location_distance_1, 10))
        self.assertTrue(check_distance(self, Location.location_distance_2, 10))
        self.assertTrue(check_distance(self, Location.location_distance_3, 10))


    def test_3_by_zip(self):
        element_invisible(self, AcceptTerms.loading)
        # click on location_icon
        element_click(self, Location.location_button)
        element_invisible(self, AcceptTerms.loading)
        #click on location navigation bar
        element_click(self, Location.location_add_button)
        element_invisible(self, AcceptTerms.loading)
        #clear text from navigation bar
        element_click(self, Location.location_clear_x)
        element_invisible(self, AcceptTerms.loading)
        #add text to navigation bar
        element_click(self, Location.location_add_text)
        element_send_text(self, Location.location_add_text, '92627')
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Location.location_city_selector)
        self.assertTrue(check_distance(self, Location.location_distance_1, 10))
        self.assertTrue(check_distance(self, Location.location_distance_2, 10))
        self.assertTrue(check_distance(self, Location.location_distance_3, 10))

if __name__ == '__main__':
    unittest.main()