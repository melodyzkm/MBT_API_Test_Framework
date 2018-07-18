"""
@Version: 1.0
@Project: F10Intro
@Author: xuruizeng
@Data: 2018/7/18
@File: f10_intro_test.py
@Description: 检查f10基本信息intro部分
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
test_url = config.get_url('f10_intro')

log = MyLog.get_log()
logger = log.get_logger()
logger.info('start run {}'.format(__file__))


class F10Intro(unittest.TestCase):
    """
    测试f10基本信息接口
    """
    def setUp(self):
        logger.info('test "{}" start'.format(test_url.format('Bitcoin')))

    def tearDown(self):
        logger.info('test "{}" end'.format(test_url.format('Bitcoin')))

    def test_f10_intro(self):
        """
        测试f10基本信息接口intro
        """
        request = ConfigRequest()
        request.set_url(test_url.format('Bitcoin'))
        response = request.get()

        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 20)
        # intro_total_supply
        self.assertIn('intro_total_supply', response)
        self.assertIsInstance(response['intro_total_supply'], str)
        self.assertGreater(len(response['intro_total_supply']), 0)
        # intro_chain
        self.assertIn('intro_chain', response)
        self.assertIsInstance(response['intro_chain'], str)
        self.assertGreater(len(response['intro_chain']), 0)
        # intro_mining
        self.assertIn('intro_mining', response)
        self.assertIsInstance(response['intro_mining'], str)
        self.assertGreater(len(response['intro_mining']), 0)
        # intro_on_market
        self.assertIn('intro_on_market', response)
        self.assertIsInstance('intro_on_market', str)
        self.assertGreater(len(response['intro_on_market']), 0)
        # intro_organization
        self.assertIn('intro_organization', response)
        self.assertIsInstance(response['intro_organization'], str)
        self.assertGreater(len(response['intro_organization']), 0)
        # intro_website
        self.assertIn('intro_website', response)
        self.assertIsInstance(response['intro_website'], str)
        self.assertGreater(len(response['intro_website']), 0)
        # intro_team
        self.assertIn('intro_team', response)
        self.assertIsInstance(response['intro_team'], str)
        self.assertGreater(len(response['intro_team']), 0)
        # intro_status
        self.assertIn('intro_status', response)
        self.assertIsInstance(response['intro_status'], str)
        self.assertGreater(len(response['intro_status']), 0)
        # ico_schedule
        self.assertIn('ico_schedule', response)
        self.assertIsInstance(response['ico_schedule'], str)
        # ico_price
        self.assertIn('ico_price', response)
        self.assertIsInstance(response['ico_price'], str)
        # ico_whitepaper
        self.assertIn('ico_whitepaper', response)
        self.assertIsInstance(response['ico_whitepaper'], str)
        self.assertGreater(len(response['ico_whitepaper']), 0)
        # ico_fund_allocation
        self.assertIn('ico_fund_allocation', response)
        self.assertIsInstance(response['ico_fund_allocation'], str)
        # ico_placement
        self.assertIn('ico_placement', response)
        self.assertIsInstance(response['ico_placement'], str)
        # ico_other_info
        self.assertIn('ico_other_info', response)
        # project_motive_solution
        self.assertIn('project_motive_solution', response)
        self.assertIsInstance(response['project_motive_solution'], str)
        self.assertGreater(len(response['project_motive_solution']), 0)
        # project_product
        self.assertIn('project_product', response)
        self.assertIsInstance(response['project_product'], str)
        self.assertGreater(len(response['project_product']), 0)
        # project_tech_highlight
        self.assertIn('project_tech_highlight', response)
        self.assertIsInstance(response['project_tech_highlight'], str)
        self.assertGreater(len(response['project_tech_highlight']), 0)
        # project_conception
        self.assertIn('project_conception', response)
        self.assertIsInstance(response['project_conception'], str)
        self.assertGreater(len(response['project_conception']), 0)
        # project_application_area
        self.assertIn('project_application_area', response)
        self.assertIsInstance(response['project_application_area'], str)
        self.assertGreater(len(response['project_application_area']), 0)
