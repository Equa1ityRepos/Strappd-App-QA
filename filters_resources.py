import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.desired_capabilities import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class MyTestCase(unittest.TestCase, ResetCapabilities):

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)

    def test_1a_shelter_defaulted_as_selected(self):
        # Shelter defaults as the selected filter
        amenities_check(self, "Shelter")

    def test_1b_select_resources(self):
        # select Resources Filter Option
        Action.element_click(Action, FilterBar.resources)
        Action.element_invisible(Action, AcceptTerms.loading)
        amenities_check(self, "Resources")

    def test_1c_sort_bar(self):
        # in sort bar All is defaulted as selected, also listed is Cloths, Hygiene, Transit and Assistance
        Action.element_invisible(Action, AcceptTerms.loading)
        Action.element_click(Action, Sort.resources_all)
        Action.element_invisible(Action, AcceptTerms.loading)
        amenities_check(self, "Resources")

    def test_2a_sort_cloths(self):
        # Select Cloths
        Action.element_click(Action, Sort.cloths)
        # In amenities list Clothing words are listed (Clothing, Cloths for Kids, Cloths)
        amenities_check(self, "Cloths")

    def test_2b_sort_hygiene(self):
        # Select Hygiene
        Action.element_click(Action, Sort.hygiene)

        # Hygiene words are in the Amenities list, "Showers", "Laundry", "Diapers", "Hygiene Kits", "Personal Supplies", "Toiletries"
        amenities_check(self, "Hygiene")

    def test_2c_sort_transit(self):
        # Select Transit
        Action.element_click(Action, Sort.transit)

        # Transit words are in the Amenities list, "Transformational Assistance", "Transitional", "Buss Pass", "Transportation", "Transportation Vouchers"
        amenities_check(self, "Transit")

    def test_2d_sort_assistance(self):
        # Select Assistance
        Action.element_click(Action, Sort.assistance)

        # Assistance words are in the Amenities list, "Advocacy", "Legal Services", "Assistiance", "Rental Assistance", "Utility Assistance"
        amenities_check(self, "Assistance")


if __name__ == '__main__':
    unittest.main()
