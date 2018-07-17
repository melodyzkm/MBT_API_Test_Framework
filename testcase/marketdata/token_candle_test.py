import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest

config = GetConfig()
base_url = config.get_url('Base_Url')
test_url = config.get_url('token_candle')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class TokenCandle(unittest.TestCase):
    """
    测试币种详情接口
    """
    def setUp(self):
        logger.info('test {} start'.format(test_url))

    def tearDown(self):
        logger.info('test {} end'.format(test_url))

    def test_token_candle(self):
        """
        测试返回数据的正确性
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin', '1d'))
        response = request.get()

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

        for item in response:
            self.assertIsInstance(item, list)
            self.assertEqual(len(item), 17)
            # time
            self.assertIsInstance(item[0], int)
            self.assertGreater(item[0], 0)
            # open
            self.assertIn(type(item[1]), [float, int])
            self.assertGreater(item[1], 0)
            # close
            self.assertIn(type(item[2]), [float, int])
            self.assertGreater(item[2], 0)
            # low
            self.assertIn(type(item[3]), [float, int])
            self.assertGreater(item[3], 0)
            # high
            self.assertIn(type(item[4]), [float, int])
            self.assertGreater(item[4], 0)
