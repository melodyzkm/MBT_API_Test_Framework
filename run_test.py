from datetime import  *
import unittest,os
from unittest.suite import TestSuite
from BeautifulReport import BeautifulReport
import shutil
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
    shutil.copy('result/%s.html'%report_name,'result/test_api_ressult.html')
    if result.failure_count or result.error_count:
        #主动出发失败导致jenkins失败
        raise Exception("主动失败，发送邮件")



if __name__ == "__main__":
    # run_test('login')
    run_test()