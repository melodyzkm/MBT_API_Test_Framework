"""
@Version: 1.0
@Project: Candle
@Author: xuruizeng
@Data: 2018/7/18
@File: candle_test.py
@Description: 检查K线
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
test_url = config.get_url('candle')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class Candle(unittest.TestCase):
    """
    测试K线接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url.format(
            'huobipro','btc-usdt','1m')))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url.format(
            'huobipro', 'btc-usdt', '1m')))

    def test_candle(self):
        """
        测试K线接口
        """
        request = ConfigRequest()
        request.set_url(test_url)
        response = request.get()

        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 0)
        for item in response:
            self.assertIsInstance(item, list)
            self.assertGreaterEqual(len(item), 15)
            # time
            self.assertIsInstance(item[0], int)
            self.assertGreater(item[0], 0)
            # open
            self.assertIn(type(item[1]), [float, int])
            self.assertGreater(item[1], 0)
            # close
            self.assertIn(type(item[2]), [float, int])
            self.assertGreater(item[2], 0)
            # high
            self.assertIn(type(item[3]), [float, int])
            self.assertGreater(item[3], 0)
            # low
            self.assertIn(type(item[4]), [float, int])
            self.assertGreater(item[4], 0)
            # volume
            self.assertIn(type(item[5]), [float, int])
            self.assertGreaterEqual(item[5], 0)
