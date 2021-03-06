"""
@Version: 1.0
@Project: QuotationRanking
@Author: xuruizeng
@Data: 2018/7/18
@File: token_quotation_ranking_test.py
@Description: 检查涨跌幅榜数据
"""


import os
import random
import unittest

from common.log import MyLog
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest
from get_config import GetConfig

config = GetConfig()
base_url = config.get_url('Base_Url')
test_url = config.get_url('token_quotation_ranking_change_ratio_24h')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class TokenQuotationRanking(unittest.TestCase):
    """
    测试涨跌幅榜接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url))

    def test_token_quotation_ranking(self):
        """
        测试涨跌幅榜接口
        """
        request = ConfigRequest()
        request.set_url(test_url)
        response = request.get()

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)
        for item in response:
            self.assertIsInstance(item, dict)

            self.assertIn('code', item)
            self.assertIsInstance(item['code'], str)
            self.assertNotEqual(item['code'], '')

            self.assertIn('name', item)
            self.assertIsInstance(item['name'], str)
            self.assertNotEqual(item['name'], '')

            self.assertIn('name_cn', item)

            self.assertIn('name_en', item)
            self.assertIsInstance(item['name_en'], str)
            self.assertNotEqual(item['name_en'], '')

            self.assertIn('name_abbr', item)
            self.assertIsInstance(item['name_abbr'], str)
            self.assertNotEqual(item['name_abbr'], '')

            self.assertIn('logo_url', item)

            self.assertIn('price', item)
            self.assertIn(type(item['price']), [float, int])
            self.assertGreater(item['price'], 0)

            self.assertIn('change_ratio', item)
            self.assertIn(type(item['change_ratio']), [float, int])

            self.assertIn('change', item)
            self.assertIn(type(item['change']), [float, int])

            self.assertIn('change_ratio_1h', item)
            self.assertIn(type(item['change_ratio_1h']), [float, int])

            self.assertIn('change_1h', item)
            self.assertIn(type(item['change_1h']), [float, int])

            self.assertIn('change_ratio_7d', item)
            self.assertIn(type(item['change_ratio_7d']), [float, int])

            self.assertIn('change_7d', item)
            self.assertIn(type(item['change_7d']), [float, int])
