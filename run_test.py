from datetime import  *
import unittest
from BeautifulReport import BeautifulReport


def main(test_suit):
    report_name = str(datetime.now().strftime("%Y%m%d_%H%M"))
    test_suite = unittest.defaultTestLoader.discover(test_suit, pattern='*test.py', top_level_dir='testcase')

    result = BeautifulReport(test_suite)
    result.report(filename=report_name, description='Login', log_path='result')

if __name__ == "__main__":
    test_suits = ['login', 'market']
    for test_suit in test_suits:
        main(test_suit)