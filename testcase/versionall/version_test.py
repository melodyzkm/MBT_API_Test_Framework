#coding=gbk
"""
@Version: 1.0
@Project: Version
@Author: long
@Data: 2018/7/19
@File: Version.py
@Description: 获取版本信息
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Version")
mylog=logfile("Version.log",type=0)

class lapVersion(TestCase):
    "获取Telegram列表"
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        '执行获取Telegram列表接口'
        url = url_base + api
        print(url)
        try:
            rep=requests.post(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True,False,msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep,dict) and len(rep)>0),True,msg=rep)

if __name__=="__main__":
    lapVersion.run()

