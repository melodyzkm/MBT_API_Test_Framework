"""
@Version: 1.0
@Project: TokenCode
@Author: xuruizeng
@Data: 2018/7/18
@File: token_code_test.py
@Description: 检查币种详情数据
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
test_url = config.get_url('token_code')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class TokenCode(unittest.TestCase):
    """
    测试币种详情接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url.format('Bitcoin')))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url.format('Bitcoin')))

    def test_token_code(self):
        """
        测试币种详情接口
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin'))
        response = request.get()

        self.assertIsInstance(response, dict)
        # code
        self.assertIn('code', response)
        self.assertIsInstance(response['code'], str)
        self.assertNotEqual(response['code'], '')
        # name
        self.assertIn('name', response)
        self.assertIsInstance(response['name'], str)
        self.assertNotEqual(response['name'], '')
        # name_cn
        self.assertIn('name_cn', response)
        # name_en
        self.assertIn('name_en', response)
        self.assertIsInstance(response['name_en'], str)
        self.assertNotEqual(response['name_en'], '')
        # name_abbr
        self.assertIn('name_abbr', response)
        self.assertIsInstance(response['name_abbr'], str)
        self.assertNotEqual(response['name_abbr'], '')
        # log_url
        self.assertIn('logo_url', response)
        self.assertIsInstance(response['logo_url'], str)
        self.assertNotEqual(response['logo_url'], '')
        # price
        self.assertIn('price', response)
        self.assertIn(type(response['price']), [float, int])
        self.assertGreater(response['price'], 0)
        # # change_ratio
        # self.assertIn('change_ratio', response)
        # self.assertIn(type(response['change_ratio']), [float, int])
        # # change
        # self.assertIn('change', response)
        # self.assertIn(type(response['change']), [float, int])
        # market_cap
        self.assertIn('market_cap', response)
        self.assertIn(type(response['market_cap']), [float, int])
        self.assertGreater(response['market_cap'], 0)
        # change_ratio_1h
        self.assertIn('change_ratio_1h', response)
        self.assertIn(type(response['change_ratio_1h']), [float, int])
        # change_ratio_7d
        self.assertIn('change_ratio_7d', response)
        self.assertIn(type(response['change_ratio_7d']), [float, int])
        # change_ratio_24h
        self.assertIn('change_ratio_24h', response)
        self.assertIn(type(response['change_ratio_24h']), [float, int])
        # circulation
        self.assertIn('circulation', response)
        self.assertIn(type(response['circulation']), [float, int])
        self.assertGreater(response['circulation'], 0)
        # turnover_24h
        self.assertIn('turnover_24h', response)
        self.assertIn(type(response['turnover_24h']), [float, int])
        self.assertGreater(response['turnover_24h'], 0)
        # time
        self.assertIn('time', response)
        self.assertIsInstance(response['time'], int)
        # update_time
        self.assertIn('update_time', response)
        self.assertIsInstance(response['update_time'], int)
