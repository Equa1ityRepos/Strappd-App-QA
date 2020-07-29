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

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)

    def test_1_card_names(self):
        #in custom functions comparing the name in list to name on card for 1st selector.
        compare_card_1(self, ResourceCards.card_1_front_page, ResourceCards.card_header_1)
        element_click(self, Header.back_arrow)
        element_invisible(self, AcceptTerms.loading)
        time.sleep(5)
        # comparing 2nd selector
        compare_card_2(self, ResourceCards.card_2_front_page, ResourceCards.card_header_2)
        element_click(self, Header.back_arrow)

    def test_2_website_card_2(self):
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.card_2_front_page)
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.website)
        time.sleep(5)
        #screenshots as proof
        ts = time.strftime("%m_%d_%Y_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts
        self.driver.save_screenshot(r"C:\Users\ginam\Desktop\strappd2\Strappd-App-QA\Screenshots/"+filename+".png")
        self.driver.press_keycode(4)
        element_click(self, Header.back_arrow)

    def test_3_facebook_card_2(self):
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.card_2_front_page)
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.facebook)
        time.sleep(5)
        #screen shots as proof
        ts = time.strftime("%m_%d_%Y_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname + ts
        self.driver.save_screenshot(r"C:\Users\ginam\Desktop\strappd2\Strappd-App-QA\Screenshots/" + filename + ".png")
        time.sleep(5)
        self.driver.press_keycode(4)
        element_click(self, Header.back_arrow)

    def test_4_map(self):
        element_invisible(self, AcceptTerms.loading)
        element_click(self, ResourceCards.card_2_front_page)
        element_invisible(self, AcceptTerms.loading)
        self.assertTrue(self, ResourceCards.map_full_screen)
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Header.back_arrow)

if __name__ == '__main__':
    unittest.main()
