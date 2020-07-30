import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep
import time
import re

class DemographicsTestCase(unittest.TestCase):

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



    def test_1_demo_men(self):
        # click on menu
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Header.menu)
        #click on men
        element_click(self, Demographics.men)
        element_invisible(self, AcceptTerms.loading)
        time.sleep(3)
        #prove that men page is pulling results for men.
        self.assertTrue(check_text(self, Demographics.men_page_1,"Men"))
        self.assertTrue(check_text(self, Demographics.men_page_2, "Men"))
        self.assertTrue(check_text(self, Demographics.men_page_3, "Men"))
        #TODO: Check with Jason about XPATH replication.

    def test_2_demo_women(self):
        click_menu(self)
        #click women
        element_click(self, Demographics.women)
        element_invisible(self, AcceptTerms.loading)
        #prove that options available are for women
        self.assertTrue(check_text(self, Demographics.woman_page_1, "Women"))
        self.assertTrue(check_text(self, Demographics.women_page_2, "Women"))
        self.assertTrue(check_text(self, Demographics.women_page_3, 'Women'))

    def test_3_demo_youth(self):
        click_menu(self)
        element_click(self, Demographics.youth)
        element_invisible(self, AcceptTerms.loading)
        # proof that Youth services are on the page.
        # self.assertTrue(check_demographics_text(self,Demographics.youth_page_1, "Youth"))
        self.assertTrue(check_text(self, Demographics.youth_page_2, 'Youth/Kids'))
        self.assertTrue(check_text(self, Demographics.youth_page_3, 'Youth/Kids'))


    def test_4_all(self):
        #navigating to all
        click_menu(self)
        element_click(self, Demographics.all)
        element_invisible(self, AcceptTerms.loading)
        # proof that all is for all
        self.assertTrue(check_text(self, Demographics.all_page_1, "Anyone"))
        self.assertTrue(check_text(self, Demographics.all_page_2, "Anyone"))
        self.assertTrue(check_text(self, Demographics.all_page_3, "Anyone"))

    def test_5_seniors(self):
        # navigating to seniors
        element_invisible(self, AcceptTerms.loading)
        click_menu(self)
        element_click(self, Demographics.seniors)
        element_invisible(self, AcceptTerms.loading)
        # proof that all is for all
        self.assertTrue(check_text(self, Demographics.seniors_page_1, "Seniors" or "Anyone"))
        self.assertTrue(check_text(self, Demographics.seniors_page_2, "Seniors"))
        self.assertTrue(check_text(self, Demographics.seniors_page_3, "Seniors"))

    def test_6_disabled(self):
        element_invisible(self, AcceptTerms.loading)
        #naviagate to disabled
        click_menu(self)
        element_click(self, Demographics.disabled)
        element_invisible(self, AcceptTerms.loading)
        #proof that services are for disabled
        self.assertTrue(check_text(self, Demographics.disabled_page_1, "Disabled"))
        self.assertTrue(check_text(self, Demographics.disabled_page_2, "Disabled"))
        self.assertTrue(check_text(self, Demographics.disabled_page_3, "Disabled"))


    def test_7_families(self):
        element_invisible(self, AcceptTerms.loading)
        #navigate to families
        click_menu(self)
        element_click(self, Demographics.families)
        element_invisible(self, AcceptTerms.loading)
        #proof is for families
        self.assertTrue(check_text(self, Demographics.families_page_1, "Families"))
        self.assertTrue(check_text(self, Demographics.families_page_2, "Families"))
        self.assertTrue(check_text(self, Demographics.families_page_3, "Families"))

    def test_8_LGBT(self):
        element_invisible(self, AcceptTerms.loading)
        # Navigate to LGBTQ+
        click_menu(self)
        element_click(self, Demographics.lgbtq)
        element_invisible(self, AcceptTerms.loading)
        # proof for LGBTQ+
        self.assertTrue(check_text(self, Demographics.lgbtq_page_1, "LGBT"))
        self.assertTrue(check_text(self, Demographics.lgbtq_page_2, "LGBT"))
        self.assertTrue(check_text(self, Demographics.lgbtq_page_3, "LGBT"))


if __name__ == '__main__':
    unittest.main()
