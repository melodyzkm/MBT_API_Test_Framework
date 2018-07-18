"""
@Version: 1.0
@Project: SymbolDetail
@Author: xuruizeng
@Data: 2018/7/18
@File: symbol_detail_test.py
@Description: 检查交易对详情数据
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
test_url = config.get_url('symbol_detail')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class SymbolDetail(unittest.TestCase):
    """
    测试交易对详情接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(
            test_url.format('huobipro', 'btc-usdt')))

    def tearDown(self):
        logger.info('test "{}" end'.format(
            test_url.format('huobipro','btc-usdt')))

    def test_symbol_detail(self):
        """
        测试交易对详情接口
        """
        request = ConfigRequest()
        request.set_url(test_url.format('huobipro', 'btc-usdt'))
        response = request.get()

        self.assertIsInstance(response, dict)
        self.assertGreaterEqual(len(response), 0)

        # market
        self.assertIn('market', response)
        self.assertIsInstance(response['market'], str)
        self.assertGreater(len(response['market']), 0)
        # symbol
        self.assertIn('symbol', response)
        self.assertIsInstance(response['symbol'], str)
        self.assertGreater(len(response['symbol']), 0)
        # time
        self.assertIn('time', response)
        self.assertIsInstance(response['time'], int)
        self.assertGreater(response['time'], 0)
        # update_time
        self.assertIn('update_time', response)
        self.assertIsInstance(response['update_time'], int)
        self.assertGreater(response['update_time'], 0)
        # open
        self.assertIn('open', response)
        self.assertIn(type(response['open']), [float, int])
        self.assertGreater(response['open'], 0)
        # close
        self.assertIn('close', response)
        self.assertIn(type(response['close']), [float, int])
        self.assertGreater(response['close'], 0)
        # high
        self.assertIn('high', response)
        self.assertIn(type(response['high']), [float, int])
        self.assertGreater(response['high'], 0)
        # low
        self.assertIn('low', response)
        self.assertIn(type(response['low']), [float, int])
        self.assertGreater(response['low'], 0)
        # volume
        self.assertIn('volume', response)
        self.assertIn(type(response['volume']), [float, int])
        self.assertGreaterEqual(response['volume'], 0)
        # amount
        self.assertIn('amount', response)
        self.assertIn(type(response['amount']), [float, int])
        self.assertGreaterEqual(response['amount'], 0)
        # market_name_cn
        self.assertIn('market_name_cn', response)
        self.assertIsInstance(response['market_name_cn'], str)
        # market_name_en
        self.assertIn('market_name_en', response)
        self.assertIsInstance(response['market_name_en'], str)
        # take_code
        self.assertIn('take_code', response)
        self.assertIsInstance(response['take_code'], str)
        # pay_code
        self.assertIn('pay_code', response)
        self.assertIsInstance(response['pay_code'], str)
        # code
        self.assertIn('code', response)
        self.assertIsInstance(response['code'], str)
        self.assertGreater(len(response['code']), 0)
        # name
        self.assertIn('name', response)
        self.assertIsInstance(response['name'], str)
        self.assertGreater(len(response['name']), 0)
        # name_en
        self.assertIn('name_en', response)
        self.assertIsInstance(response['name_en'], str)
        # name_cn
        self.assertIn('name_cn', response)
        self.assertIsInstance(response['name_cn'], str)
        # name_abbr
        self.assertIn('name_abbr', response)
        self.assertIsInstance(response['name_abbr'], str)
        # logo_url
        self.assertIn('logo_url', response)
        self.assertIsInstance(response['logo_url'], str)
