import unittest
from appium import webdriver
from tools.helper_functions.custom_functions import *
# from tools.helper_functions.filters_helpers import *
from tools.global_data import *
from tools.ex_conds import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class OptionsPageTestCase(unittest.TestCase):  # make sure to include TestCase

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

    # copy everything to here for new pages i guess
    def test_0_onboarding(self):
        get_through_onboarding(self)

    # select about and then go back to main page
    def test_1_about_page(self):
        element_invisible(self, AcceptTerms.loading)
        element_click(self, Header.menu)
        element_click(self, Options.about_strappd)
        element_click(self, Options.back_arrow_about)

    # select crisis lines and go back to main page
    def test_2_crisis_lines(self):
        element_invisible(self, AcceptTerms.loading)
        click_menu(self)
        element_click(self, Options.crisis_lines)
        element_click(self, Options.back_arrow_crisis)

    # navigate to feedback and then back to main page
    def test_3_feedback(self):
        element_invisible(self, AcceptTerms.loading)
        click_menu(self)
        element_click(self, Options.give_feedback)
        element_send_text(self, Options.feedback_email_field, 'email field')
        element_send_text(self, Options.feedback_subject_field, 'subject field')
        element_send_text(self, Options.feedback_message_field, 'message field')
        if self.driver.find_element_by_xpath(r'//android.view.View[@content-desc="Send Feedback"]').is_enabled():
            print('send feedback button enabled')
        element_click(self, Options.back_arrow_give_feedback)

    # navigate to terms of use and back to main page
    def test_4_terms_of_use_privacy(self):
        element_invisible(self, AcceptTerms.loading)
        click_menu(self)
        element_click(self, Options.terms_and_privacy)
        element_click(self, Options.back_arrow_terms_and_privacy)

    # navigate to provider login and click cancel button
    def test_5_provider_login_simple(self):
        element_invisible(self, AcceptTerms.loading)
        click_menu(self)
        element_click(self, Options.provider_login)
        time.sleep(5)
        element_click(self, Options.cancel_button_provider_login)

    #menu drawer slides over and returns to resource cards upon hitting back button
    def test_6_menu_drawer(self):
        element_invisible(self, AcceptTerms.loading)
        time.sleep(5)
        click_menu(self)
        element_click(self, Options.menu_drawer_back)
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()
