import unittest
import logging
import sys
import os

import server.test.modelstest as models

test_classes = [
    models.ModelsTest,
]

# set up all logging to DEBUG (cause we're running tests here!)
logging.basicConfig(level=logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler = logging.FileHandler(os.path.join('logs', 'test.log'))
log_handler.setFormatter(log_formatter)

# now run all the tests
suites = [unittest.TestLoader().loadTestsFromTestCase(test_class) for test_class in test_classes]

if __name__ == "__main__":
    suite = unittest.TestSuite(suites)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not test_result.wasSuccessful():
        sys.exit(1)
