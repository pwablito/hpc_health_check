import unittest
import tests.config


def run_tests():
    # TODO Figure out how to combine test suites
    unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromModule(tests.config)
    )
