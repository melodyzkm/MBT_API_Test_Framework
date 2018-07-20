"""
@Version: 1.0
@Project: Home Page
@Author: Zhang Kaiming
@Data: 2018/7/20
@Description: 检查首页主表的排序功能
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


class HomepageSort(unittest.TestCase):

    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test end")

    def test_rankings_change(self):
        api = config.get_url("homepage_sort")
        request = ConfigRequest()
        l_sort_direction = ["asc", "desc"]
        l_sort_item = ["cmc_volume_usd", "chain_new_user_count_7day", "git_commit_count_7day", "git_commit_count_30day",
                       "git_contributor_count", "market_cap_usd", "twitter_follower_count"]

        for direction in l_sort_direction:
            for item in l_sort_item:
                params = {"skip": 0, "limit": 20, "sort": "{} {}".format(item, direction)}
                request.set_url(api)
                request.set_params(params)
                response = request.get()

                # return 20 tokens
                self.assertEqual(len(response), 20)
                for token in response:
                    self.assertNotEqual(token.get("name"), None)
                    self.assertNotEqual(token.get("name_abbr"), None)
                    self.assertNotEqual(token.get("cmc_market_cap_usd"), None)
                    self.assertNotEqual(token.get("cmc_price_usd"), None)
                    self.assertNotEqual(token.get("cmc_volume_usd"), None)
                    # self.assertNotEqual(token.get("git_commit_count_7day"), None)
                    # self.assertNotEqual(token.get("git_commit_count_30day"), None)
                    # self.assertNotEqual(token.get("chain_new_user_count_7day"), None)
                    # self.assertNotEqual(len(token.get("price_7d")), 0)


