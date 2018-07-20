"""
@Version: 1.0
@Project: Home Page
@Author: Zhang Kaiming
@Data: 2018/7/10
@Description: 检查市值前十的货币
"""


import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest

config = GetConfig()
market_cap_ratio_api = "/api/v1/home/market_cap_ratio"

log = MyLog.get_log()
logger = log.get_logger()

class MarketcapRatio(unittest.TestCase):

    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test end")
        
    def test_amount_of_return_data(self):
        """
        检查可以正确返回货币的个数
        """

        request = ConfigRequest()
        request.set_url(market_cap_ratio_api)
        response = request.get()

        self.assertEqual(len(response), 10)

    def test_data(self):
        """
        检查返回数据的正确性
        """

        db_bcf = BcfMongo()
        request = ConfigRequest()
        request.set_url(market_cap_ratio_api)
        response = request.get()

        first_cap_coin = response[0]
        first_cap_coin_code= first_cap_coin.get("code")
        first_cap_coin_cap= first_cap_coin.get("cmc_market_cap_usd")

        btc_cap = db_bcf.get_cmc_indicators_with_code("Bitcoin", "cmc_market_cap_usd")

        self.assertEqual(first_cap_coin_code, "Bitcoin")
        self.assertEqual(first_cap_coin_cap, btc_cap)


    def test_data_field(self):
        """
        检查所有的字段都不为空
        """

        request = ConfigRequest()
        request.set_url(market_cap_ratio_api)
        response = request.get()

        for item in response:
            self.assertNotEqual(item.get("name"), None)
            self.assertNotEqual(item.get("name"), "")
