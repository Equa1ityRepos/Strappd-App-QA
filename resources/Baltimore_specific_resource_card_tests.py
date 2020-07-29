import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class ResourceCardDetailsTestCases(unittest.TestCase, Action):

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

    # TODO: HI JASON! If you want to check these tests you'll have to find specific xpaths for email, and phone.

    def test_1_phone_number_manna(self): #THIS TEST IS LOCATION SPECIFIC AND WILL NOT WORK ANYWHERE BUT BALTIMORE
        element_invisible(self, AcceptTerms.loading)
        time.sleep(5)
        self.driver.swipe(380,259,280,659)
        element_click(self, ResourceCards.card_1_front_page)
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.card_1_phone)
        time.sleep(2)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        time.sleep(5)
        element_click(self, Header.back_arrow)

    def test_2_email_manna(self): #THIS TEST IS LOCATION SPECIFIC AND WILL NOT WORK ANYWHERE BUT BALTIMORE
        element_invisible(self, AcceptTerms.loading)
        time.sleep(4)
        element_click(self, ResourceCards.card_1_front_page)
        element_invisible(self, AcceptTerms.loading)
        time.sleep(3)
        element_click(self, ResourceCards.email_manna)
        activity = self.driver.current_activity
        print(activity)
        time.sleep(3)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        element_click(self, Header.back_arrow)

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)


if __name__ == '__main__':
    unittest.main()
