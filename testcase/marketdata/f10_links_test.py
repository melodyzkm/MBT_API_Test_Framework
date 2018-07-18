"""
@Version: 1.0
@Project: F10Links
@Author: xuruizeng
@Data: 2018/7/18
@File: f10_links_test.py
@Description: 检查f10基本信息links部分
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
test_url = config.get_url('f10_links')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class F10Links(unittest.TestCase):
    """
    测试f10基本信息接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url.format('Bitcoin')))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url.format('Bitcoin')))

    def test_f10_links(self):
        """
        测试f10基本信息接口links
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin'))
        response = request.get()

        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 14)
        # bitcointalk
        self.assertIn('bitcointalk', response)
        self.assertIsInstance(response['bitcointalk'], list)
        # explorer
        self.assertIn('explorer', response)
        self.assertIsInstance(response['explorer'], list)
        # facebook
        self.assertIn('facebook', response)
        self.assertIsInstance(response['facebook'], list)
        # forum
        self.assertIn('forum', response)
        self.assertIsInstance(response['forum'], list)
        # github
        self.assertIn('github', response)
        self.assertIsInstance(response['github'], list)
        # telegram
        self.assertIn('telegram', response)
        self.assertIsInstance(response['telegram'], list)
        # twitter
        self.assertIn('twitter', response)
        self.assertIsInstance(response['twitter'], list)
        # website
        self.assertIn('website', response)
        self.assertIsInstance(response['website'], list)
        # wechat
        self.assertIn('wechat', response)
        self.assertIsInstance(response['wechat'], list)
        # whitepaper
        self.assertIn('whitepaper', response)
        self.assertIsInstance(response['whitepaper'], list)
        # coinmarketcap
        self.assertIn('coinmarketcap', response)
        self.assertIsInstance(response['coinmarketcap'], list)
        # feixiaohao
        self.assertIn('feixiaohao', response)
        self.assertIsInstance(response['feixiaohao'], list)
        # reddit
        self.assertIn('reddit', response)
        self.assertIsInstance(response['reddit'], list)
        # block
        self.assertIn('block', response)
        self.assertIsInstance(response['block'], list)
