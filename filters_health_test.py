import unittest
from appium import webdriver
from tools.ex_conds import *
from tools.desired_capabilities import *
from tools.helper_functions.custom_functions import *
from tools.helper_functions.filters_helpers import *
from time import sleep


class FiltersHealthTest(unittest.TestCase, ResetCapabilities):
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_0_skip_onboarding(self):
        get_through_onboarding(self)

    def test_1a_shelter_defaulted_as_selected(self):
        # Shelter defaults as the selected filter
        amenities_check(self, FilterBar.shelter)

    def test_2a_health_filter(self):
        # Select Health Filter
        amenities_check(self, FilterBar.health)
        # in sort bar All is defaulted as selected, also listed isMedical and Counseling
        Action.element_visible(Action, Sort.medical)
        Action.element_visible(Action, Sort.counseling)

    def test_2b_medical_sort(self):
        # Select Medical
        # In amenities list Medical words are listed ("Clinic, HIV Testing, Syringe Access, Medical Clinic, Medical, prescriptions, health, Dental, immunizations, Well Child Checks, Urgent Medical Assistance")
        amenities_check(self, Sort.medical)

    def test_2c_counseling_sort(self):
        # Select Counseling
        # Counseling words are in the Amenities list, "Counseling", "Substance Abuse Treatment", "Therapy", "Treatment", "Mental Health", "Behavior")
        amenities_check(self, Sort.counseling)


if __name__ == '__main__':
    unittest.main()
