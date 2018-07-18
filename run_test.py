from datetime import  *
import unittest,os
from unittest.suite import TestSuite
from BeautifulReport import BeautifulReport
from common.emailsender import MYEMAIL


def run_test(path:str='testcase'):
    """
    :param path: With default path testcase, the method will execute all testcases, otherwise it only execute the
    cases which in the specific path
    :return: test report
    """
    report_name = "{}_{}".format(path, str(datetime.now().strftime("%Y%m%d%H%M")))
    testsuits = TestSuite()

    if path == 'testcase':
        for dir in os.listdir(os.path.join(os.curdir, path)):
            testsuits.addTests(unittest.defaultTestLoader.discover(dir, pattern='*test.py', top_level_dir='testcase'))
    else:
        testsuits.addTests(unittest.defaultTestLoader.discover(path, pattern='*test.py', top_level_dir='testcase'))

    result = BeautifulReport(testsuits)
    result.report(filename=report_name, description=path, log_path='result')


if __name__ == "__main__":
    # run_test('login')
    run_test()