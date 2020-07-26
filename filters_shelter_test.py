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
        #In Resource Card's Amenities list Shelter is listed
        amenities_check(self, FilterBar.shelter)

        # in sort bar All is defaulted as selected, also listed is Emergency and Transitional
        Action.element_visible(Action, Sort.emergency)
        Action.element_visible(Action, Sort.transitional)

    def test_2a_sort_emergency(self):
        # Select Emergency
        # In amenities list Emergency words are listed
        amenities_check(self, Sort.emergency)

    def test_2b_sort_transitional(self):
        # Select Transitional
        # Transitional words are in the Resources list, "Day", "Evening", "Transitional"
        amenities_check(self, Sort.transitional)


if __name__ == '__main__':
    unittest.main()
