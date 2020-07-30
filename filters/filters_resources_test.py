import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class FiltersResourcesTestCase(unittest.TestCase):

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

    def test_1a_shelter_defaulted_as_selected(self):
        # Shelter defaults as the selected filter
        amenities_check(self, FilterBar.shelter)

    def test_1b_select_resources(self):
        # select Resources Filter Option
        amenities_check(self, FilterBar.resources)

    def test_1c_sort_bar(self):
        # in sort bar All is defaulted as selected, also listed is Cloths, Hygiene, Transit and Assistance
        amenities_check(self, FilterBar.resources)

    def test_2a_sort_cloths(self):
        # Select Cloths
        element_click(self, Sort.cloths)
        # In amenities list Clothing words are listed (Clothing, Cloths for Kids, Cloths)
        amenities_check(self, Sort.cloths)

    def test_2b_sort_hygiene(self):
        # Select Hygiene
        element_click(self, Sort.hygiene)

        # Hygiene words are in the Amenities list, "Showers", "Laundry", "Diapers", "Hygiene Kits", "Personal Supplies", "Toiletries"
        amenities_check(self, Sort.hygiene)

    def test_2c_sort_transit(self):
        # Select Transit
        element_click(self, Sort.transit)

        # Transit words are in the Amenities list, "Transformational Assistance", "Transitional", "Buss Pass", "Transportation", "Transportation Vouchers"
        amenities_check(self, Sort.transit)

    def test_2d_sort_assistance(self):
        # Select Assistance
        element_click(self, Sort.assistance)

        # Assistance words are in the Amenities list, "Advocacy", "Legal Services", "Assistiance", "Rental Assistance", "Utility Assistance"
        amenities_check(self, Sort.assistance)


if __name__ == '__main__':
    unittest.main()
