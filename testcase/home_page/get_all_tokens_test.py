# -*- coding: UTF-8 -*-
"""
@Version: 1.0
@Project: Home Page
@Author: Zhang Kaiming
@Data: 2018/7/20
@Description: 检查获取所有token的接口
"""


import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()
all_token_api = config.get_url("Get_Token_All")

log = MyLog.get_log()
logger = log.get_logger()

class GetAllToken(unittest.TestCase):
    "获取token列表"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        """
        检查返回正确的token数据
        """

        request = ConfigRequest()
        request.set_url(all_token_api)
        response = request.get()

        tokens_amount = len(response)
        self.assertGreater(tokens_amount, 1400)
        for token in response:
            self.assertNotEqual(token.get("name"), None)
            self.assertNotEqual(token.get("name_en"), None)



