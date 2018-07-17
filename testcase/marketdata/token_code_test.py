import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest

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
        logger.info('test {} start'.format(test_url))

    def tearDown(self):
        logger.info('test {} end'.format(test_url))

    def test_token_code(self):
        """
        测试返回数据的正确性
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin'))
        response = request.get()

        self.assertIsInstance(response, dict)

        self.assertIn('code', response)
        self.assertIsInstance(response['code'], str)
        self.assertNotEqual(response['code'], '')

        self.assertIn('name', response)
        self.assertIsInstance(response['name'], str)
        self.assertNotEqual(response['name'], '')

        self.assertIn('name_cn', response)

        self.assertIn('name_en', response)
        self.assertIsInstance(response['name_en'], str)
        self.assertNotEqual(response['name_en'], '')

        self.assertIn('name_abbr', response)
        self.assertIsInstance(response['name_abbr'], str)
        self.assertNotEqual(response['name_abbr'], '')

        self.assertIn('logo_url', response)
        self.assertIsInstance(response['logo_url'], str)
        self.assertNotEqual(response['logo_url'], '')

        self.assertIn('price', response)
        self.assertIn(type(response['price']), [float, int])
        self.assertGreater(response['price'], 0)

        self.assertIn('change_ratio', response)
        self.assertIn(type(response['change_ratio']), [float, int])

        self.assertIn('change', response)
        self.assertIn(type(response['change']), [float, int])

        self.assertIn('market_cap', response)
        self.assertIn(type(response['market_cap']), [float, int])
        self.assertGreater(response['market_cap'], 0)

        self.assertIn('change_ratio_1h', response)
        self.assertIn(type(response['change_ratio_1h']), [float, int])

        self.assertIn('change_ratio_7d', response)
        self.assertIn(type(response['change_ratio_7d']), [float, int])

        self.assertIn('change_ratio_24h', response)
        self.assertIn(type(response['change_ratio_24h']), [float, int])

        self.assertIn('circulation', response)
        self.assertIn(type(response['circulation']), [float, int])
        self.assertGreater(response['circulation'], 0)

        self.assertIn('turnover_24h', response)
        self.assertIn(type(response['turnover_24h']), [float, int])
        self.assertGreater(response['turnover_24h'], 0)

        self.assertIn('time', response)
        self.assertIsInstance(response['time'], int)

        self.assertIn('update_time', response)
        self.assertIsInstance(response['update_time'], int)
