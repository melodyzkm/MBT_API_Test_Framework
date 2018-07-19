"""
@Version: 1.0
@Project: SymbolRanking
@Author: xuruizeng
@Data: 2018/7/18
@File: symbol_ranking_test.py
@Description: 检查交易对排行数据
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
test_url = config.get_url('symbol_rank')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class SymbolRanking(unittest.TestCase):
    """
    测试交易对排行接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url))

    def test_symbol_ranking(self):
        """
        测试交易对排行接口
        """
        request = ConfigRequest()
        request.set_url(test_url)
        response = request.get()

        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 0)

        for item in response:
            self.assertIsInstance(item, dict)
            self.assertGreaterEqual(len(item), 20)
            # time
            self.assertIn('time', item)
            self.assertIsInstance(item['time'], int)
            self.assertGreater(item['time'], 0)
            # update_time
            self.assertIn('update_time', item)
            self.assertIsInstance(item['update_time'], int)
            self.assertGreater(item['update_time'], 0)
            # open
            self.assertIn('open', item)
            self.assertIn(type(item['open']), [float, int])
            self.assertGreater(item['open'], 0)
            # close
            self.assertIn('close', item)
            self.assertIn(type(item['close']), [float, int])
            self.assertGreater(item['close'], 0)
            # high
            self.assertIn('high', item)
            self.assertIn(type(item['high']), [float, int])
            self.assertGreater(item['high'], 0)
            # low
            self.assertIn('low', item)
            self.assertIn(type(item['low']), [float, int])
            self.assertGreater(item['low'], 0)
            # volume
            self.assertIn('volume', item)
            self.assertIn(type(item['volume']), [float, int])
            self.assertGreaterEqual(item['volume'], 0)
            # amount
            self.assertIn('amount', item)
            self.assertIn(type(item['amount']), [float, int])
            self.assertGreaterEqual(item['amount'], 0)
            # market
            self.assertIn('market', item)
            self.assertIsInstance(item['market'], str)
            self.assertGreater(len(item['market']), 0)
            # symbol
            self.assertIn('symbol', item)
            self.assertIsInstance(item['symbol'], str)
            self.assertGreater(len(item['symbol']), 0)

            # market_name_cn
            self.assertIn('market_name_cn', item)
            #self.assertIsInstance(item['market_name_cn'], str)
            # market_name_en
            self.assertIn('market_name_en', item)
            self.assertIsInstance(item['market_name_en'], str)
            # take_code
            self.assertIn('take_code', item)
            self.assertIsInstance(item['take_code'], str)
            # pay_code
            self.assertIn('pay_code', item)
            self.assertIsInstance(item['pay_code'], str)
            # code
            self.assertIn('code', item)
            self.assertIsInstance(item['code'], str)
            self.assertGreater(len(item['code']), 0)
            # name
            self.assertIn('name', item)
            self.assertIsInstance(item['name'], str)
            self.assertGreater(len(item['name']), 0)
            # name_en
            self.assertIn('name_en', item)
            self.assertIsInstance(item['name_en'], str)
            # name_cn
            self.assertIn('name_cn', item)
            #self.assertIsInstance(item['name_cn'], str)
            # name_abbr
            self.assertIn('name_abbr', item)
            self.assertIsInstance(item['name_abbr'], str)
            # price
            self.assertIn('price', item)
            self.assertIn(type(item['price']), [float, int])
            self.assertGreater(item['price'], 0)
