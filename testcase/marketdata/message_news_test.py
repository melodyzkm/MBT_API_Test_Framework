"""
@Version: 1.0
@Project: MessageNews
@Author: xuruizeng
@Data: 2018/7/18
@File: message_news_test.py
@Description: 检查新闻数据
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
test_url = config.get_url('message_news')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class MessageNews(unittest.TestCase):
    """
    测试新闻接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url.format('Bitcoin')))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url.format('Bitcoin')))

    def test_token_candle(self):
        """
        测试新闻接口
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin'))
        response = request.get()

        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

        for item in response:
            self.assertIsInstance(item, dict)
            self.assertEqual(len(item), 7)
            # new_id
            self.assertIn('news_id', item)
            self.assertIsInstance(item['news_id'], str)
            self.assertGreater(len(item['news_id']), 0)
            # source_time
            self.assertIn('source_time', item)
            self.assertIsInstance(item['source_time'], str)
            self.assertGreater(len(item['source_time']), 0)
            # create_time
            self.assertIn('create_time', item)
            self.assertIsInstance(item['create_time'], str)
            self.assertGreater(len(item['create_time']), 0)
            # title
            self.assertIn('title', item)
            self.assertIsInstance(item['title'], str)
            # content
            self.assertIn('content', item)
            self.assertIsInstance(item['content'], str)
            self.assertGreater(len(item['content']), 0)
            # language
            self.assertIn('language', item)
            self.assertIsInstance(item['language'], str)
            # self.assertIn(item['language'], ['zh-cn',''])
            # link
            self.assertIn('link', item)
            self.assertIsInstance(item['link'], str)
