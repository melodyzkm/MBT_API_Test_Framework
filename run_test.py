from datetime import  *
import unittest,os
from BeautifulReport import BeautifulReport
from common.emailsender import MYEMAIL
me=MYEMAIL()
def main(test_suit):
    report_name = str(datetime.now().strftime("%Y%m%d_%H%M"))
    test_suite = unittest.defaultTestLoader.discover(test_suit, pattern='*test.py', top_level_dir='testcase')

    result = BeautifulReport(test_suite)
    result.report(filename=report_name, description=test_suit, log_path='result')
    # try:
    #     me.email_file(filename=os.path.join(os.curdir,'result',report_name+'.html'),showname='自动化报告.html',subject='自动化测试报告',sendername='自动化机器人')
    # except:
    #     pass
if __name__ == "__main__":
    path,dir,file=list(os.walk(os.path.join(os.curdir,'testcase')))[0]
    # test_suits = dir
    test_suits=['alltoken']
    for test_suit in test_suits:
        main(test_suit)
