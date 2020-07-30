import unittest

# import test modules
from tools.global_data import *
from filters.filters_work_test import FiltersWorkTestCase
from filters.filters_food_test import FiltersFoodTestCase
from filters.filters_resources_test import FiltersResourcesTestCase
from filters.filters_shelter_test import FiltersShelterTestCase
from filters.filters_health_test import FiltersHealthTestCase

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromTestCase(FiltersShelterTestCase))
suite.addTests(loader.loadTestsFromTestCase(FiltersHealthTestCase))
suite.addTests(loader.loadTestsFromTestCase(FiltersResourcesTestCase))
suite.addTests(loader.loadTestsFromTestCase(FiltersFoodTestCase))
suite.addTests(loader.loadTestsFromTestCase(FiltersWorkTestCase))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
