import unittest
from simplest.chrome import RunChromeTests

tests_for_chrome = unittest.defaultTestLoader.loadTestsFromTestCase(RunChromeTests)

test_suite = unittest.TestSuite([tests_for_chrome])

unittest.TextTestRunner(verbosity=2).run(test_suite)
