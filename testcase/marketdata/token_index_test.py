"""
@Version: 1.0
@Project: TokenIndex
@Author: xuruizeng
@Data: 2018/7/18
@File: token_index_test.py
@Description: 检查首页数据
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
test_url = config.get_url('token_index')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))

class TokenIndex(unittest.TestCase):
    """
    测试首页接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url))

    def check_indicators(self, items):
        """
        测试indicators
        """
        b_ret = True

        self.assertEqual(len(items), 3)

        for item in items:
            self.assertEqual(type(item), dict)

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

            self.assertIn('value', item)
            self.assertIn(type(item['value']), [float, int])
            self.assertGreater(item['value'], 0)

            # self.assertIn('change', item)
            # self.assertIn(type(item['change']), [float, int])

            # self.assertIn('change_ratio', item)
            # self.assertIn(type(item['change_ratio']), [float, int])

        return b_ret

    def check_rise_rank(self, items):
        """
        测试rise_rank各项数据
        """
        b_ret = True

        self.assertGreater(len(items), 0)

        for item in items:
            self.assertEqual(type(item), dict)

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
            # self.assertIsNotNone(item['logo_url'])

            self.assertIn('price', item)
            self.assertIn(type(item['price']), [float, int])
            self.assertGreater(item['price'], 0)

            # self.assertIn('change_ratio', item)
            # self.assertIn(type(item['change_ratio']), [float, int])

            # self.assertIn('change', item)
            # self.assertIn(type(item['change']), [float, int])

            self.assertIn('change_ratio_1h', item)
            self.assertIn(type(item['change_ratio_1h']), [float, int])

            self.assertIn('change_1h', item)
            self.assertIn(type(item['change_1h']), [float, int])

            self.assertIn('change_ratio_7d', item)
            self.assertIn(type(item['change_ratio_7d']), [float, int])

            self.assertIn('change_7d', item)
            self.assertIn(type(item['change_7d']), [float, int])

        return b_ret

    def check_drop_rank(self, items):
        """
        测试indicator各项数据
        """
        b_ret = True

        self.assertEqual(len(items), 5)

        for item in items:
            self.assertEqual(type(item), dict)

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
            self.assertIsNotNone(item['logo_url'])

            self.assertIn('price', item)
            self.assertIn(type(item['price']), [float, int])
            self.assertGreater(item['price'], 0)

            # self.assertIn('change_ratio', item)
            # self.assertIn(type(item['change_ratio']), [float, int])

            # self.assertIn('change', item)
            # self.assertIn(type(item['change']), [float, int])

            # self.assertIn('change_ratio_1h', item)
            # self.assertIn(type(item['change_ratio_1h']), [float, int])

            # self.assertIn('change_1h', item)
            # self.assertIn(type(item['change_1h']), [float, int])

            # self.assertIn('change_ratio_7d', item)
            # self.assertIn(type(item['change_ratio_7d']), [float, int])

            # self.assertIn('change_7d', item)
            # self.assertIn(type(item['change_7d']), [float, int])

        return b_ret

    def test_token_index(self):
        """
        测试首页接口
        """
        request = ConfigRequest()
        request.set_url(test_url)
        response = request.get()

        self.assertIsInstance(response, dict)

        self.assertIn('indicators', response)
        self.assertTrue(self.check_indicators(response['indicators']))

        self.assertIn('up_count', response)
        self.assertIsInstance(response['up_count'], int)
        self.assertGreaterEqual(response['up_count'], 0)

        self.assertIn('down_count', response)
        self.assertIsInstance(response['down_count'], int)
        self.assertGreaterEqual(response['down_count'], 0)

        self.assertIn('rise_rank', response)
        self.assertTrue(self.check_rise_rank(response['rise_rank']))

        self.assertIn('drop_rank', response)
        self.assertTrue(self.check_drop_rank(response['drop_rank']))

        self.assertIn('time', response)
        self.assertIsInstance(response['time'], int)
