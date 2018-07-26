#coding=utf-8

"""
@Version: 1.0
@Project: twitter
@Author: long
@Data: 2018/7/20
@File: twitter_test.py
@Description: 获取twitter列表
"""

from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig
import time

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Twitter")
# mylog=logfile("twitter.log",type=0)

class LapTwitter(TestCase):
    "获取twitter列表"
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check(self,token,lau,ts,size):
        '执行twitter列表接口获取最新的N条（默认50）'
        url = url_base + api.format(token,lau,ts,size)
        try:
            rep=requests.get(url).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True,False,msg=e)

        # mylog.info(rep)

        self.assertEqual((isinstance(rep,list)),True,msg=rep)

        #判断按照ID进行排序
        st_list=[i.get("source_time") for i in rep]
        self.assertListEqual(sorted(st_list,reverse=-1),st_list,msg="消息没有按照时间排序")

        for item in rep:
            '''
            1.content不为空
            2.content为字符串类型
            '''
            self.assertIn("text",item)
            # self.assertIsInstance(item.get("message",None),str)
            # self.assertIsNot(item.get("message",None),"")

            self.assertEqual(item.get("code", None),token)

            self.assertIsInstance(item.get("source_time", None), str)
            self.assertIsNot(item.get("source_time", None), "")
            self.assertRegex(item.get("source_time", None),r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.000Z',msg="时间格式返回不正确")

            self.assertIsInstance(item.get("id", None), str)
            self.assertIsNot(item.get("id",None), "")

    def test_001_get(self):
        """获取BTC的twitter信息"""
        ts=int(time.time())*1000
        self.check("Bitcoin","cn",ts,50)

    def test_002_get(self):
        """获取REQ的twitter信息"""
        ts=int(time.time())*1000
        self.check("0x8f8221afbb33998d8584a2b05749ba73c37a938a","cn",ts,50)

    def test_003_get(self):
        """获取BTC的twitter英文信息"""
        ts=int(time.time())*1000
        self.check("Bitcoin","en",ts,50)

if __name__=="__main__":
    LapTwitter.run()

