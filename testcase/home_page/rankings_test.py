"""
@Version: 1.0
@Project: Home Page
@Author: Zhang Kaiming
@Data: 2018/7/20
@Description: 检查首页的排行榜功能
"""

import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest

config = GetConfig()

log = MyLog.get_log()
logger = log.get_logger()


class Rankings(unittest.TestCase):

    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test end")

    def rankings_change(self, url):

        request = ConfigRequest()
        request.set_url(url)

        # Descending
        request.set_params({"sort": "desc", "limit": 10})
        response = request.get()

        # return 10 tokens
        self.assertEqual(len(response), 10)
        for token in response:
            self.assertNotEqual(token.get("cmc_change_ratio"), None)
            self.assertNotEqual(token.get("cmc_price_usd"), None)
            self.assertNotEqual(token.get("name"), None)

        # Ascending
        request.set_params({"sort": "asc", "limit": 10})
        response = request.get()

        # return 10 tokens
        self.assertEqual(len(response), 10)
        for token in response:
            self.assertNotEqual(token.get("cmc_change_ratio"), None)
            self.assertNotEqual(token.get("cmc_price_usd"), None)
            self.assertNotEqual(token.get("name"), None)

    def test_rankings_change_1h(self):
        """
        检查按1h涨跌幅排序
        """
        self.rankings_change("/api/v1/home/ranking/change_ratio_1h")

    def test_rankings_change_24h(self):
        """
        检查按1h涨跌幅排序
        """
        self.rankings_change("/api/v1/home/ranking/change_ratio_24h")

    def test_rankings_volume_24h(self):
        api = "/api/v1/home/ranking/volume_24h"
        request = ConfigRequest()
        request.set_url(api)

        request.set_params({"sort": "desc", "limit": 10})
        response = request.get()

        # return 10 tokens
        self.assertEqual(len(response), 10)
        for token in response:
            self.assertNotEqual(token.get("cmc_volume_usd"), None)
            self.assertNotEqual(token.get("name"), None)

