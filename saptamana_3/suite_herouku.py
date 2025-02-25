import unittest

import HtmlTestRunner

from saptamana_3.alerte_herouku import TestAlert
from saptamana_3.keys_herouku import TestKeys

# html-testRunner
#  pip install html-testRunner
class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlert))

        # test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestAlert), unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Titlu raport executie",
            report_name="Rezultate teste"
        )
        runner.run(test_suite)
