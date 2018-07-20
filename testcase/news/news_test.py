# -*- coding: UTF-8 -*-
"""
@Version: 1.0
@Project:
@Author: Zhang Kaiming
@Data: 2018/7/20
@Description: 检查新闻接口
"""


import time, datetime
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()
news_api = config.get_url("news")

log = MyLog.get_log()
logger = log.get_logger()

class GetNews(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        """
        检查返回正确的token数据
        """

        request = ConfigRequest()
        languages = ["cn", "en"]
        ONE_HOUR = 3600

        for lang in languages:
            params = {"lang": lang}
            request.set_params(params)
            request.set_url(news_api)
            response = request.get()

            tokens_amount = len(response)
            self.assertEqual(tokens_amount, 50)
            last_news_time = response[0].get("create_time")
            last_news_time = datetime.datetime.strptime(last_news_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            now = datetime.datetime.utcnow()
            timedelta = now - last_news_time

            # The last news was updated recently
            print("Last news was updated at {}, now {}".format(last_news_time, now))
            self.assertLess(timedelta.seconds, ONE_HOUR)


