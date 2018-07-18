"""
@Version: 1.0
@Project: SymbolIndex
@Author: xuruizeng
@Data: 2018/7/18
@File: symbol_index_test.py
@Description: 检查交易对首页头部指数数据
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
test_url = config.get_url('symbol_index')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class SymbolIndex(unittest.TestCase):
    """
    测试交易对首页接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url))

    def test_symbol_list(self):
        """
        测试交易对首页接口
        """
        request = ConfigRequest()
        request.set_url(test_url)
        response = request.get()

        self.assertIsInstance(response, dict)
        self.assertIn('indicators', response)
        self.assertIsInstance(response['indicators'], list)
        self.assertGreater(len(response['indicators']), 0)
        for item in response['indicators']:
            self.assertIsInstance(item, dict)
            self.assertEqual(len(item), 16)
            # code
            self.assertIn('code', item)
            self.assertIsInstance(item['code'], str)
            self.assertNotEqual(item['code'], '')
            # name
            self.assertIn('name', item)
            self.assertIsInstance(item['name'], str)
            self.assertNotEqual(item['name'], '')
            # name_cn
            self.assertIn('name_cn', item)
            # name_en
            self.assertIn('name_en', item)
            self.assertIsInstance(item['name_en'], str)
            self.assertNotEqual(item['name_en'], '')
            # name_abbr
            self.assertIn('name_abbr', item)
            self.assertIsInstance(item['name_abbr'], str)
            self.assertNotEqual(item['name_abbr'], '')
