"""
@Version: 1.0
@Project: LoginTest
@Author: Kevin Chang
@Data: 2018/7/12
@File: login_logout_test.py
@Description: 检查是否可以登录退出
"""


import random
import os
import time
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()
base_url = config.get_url("Base_Url")
log = MyLog.get_log()
logger = log.get_logger()

class LoginLogout(unittest.TestCase):

    def setUp(self):
        self.token = ""
        print("Test start")

    def tearDown(self):
        print("Test end")

    def test_login(self):
        """
        检查可以正确登录
        """

        mobile = config.get_login("Mobile")
        valid = config.get_login("Valid")
        ts = time.time()

        api = config.get_url("Login")
        request = ConfigRequest()
        request.set_url(api)
        request.set_data({"mobile":mobile, "valid": valid})
        response = request.post()
        self.token = response.get('token')



        self.assertEqual(response.get("code"), 0)
        # 7天后过期
        self.assertAlmostEqual(response.get("exp"), ts + 7*24*60*60, delta=10)
        # token长度
        self.assertIn(len(response.get('token')), [i for i  in range(100, 256)])

    def test_logout(self):
        """
        检查可以正确退出
        """
        mobile = config.get_login("Mobile")
        valid = config.get_login("Valid")

        api_in = config.get_url("Login")
        api_out = config.get_url("Logout")
        request_in = ConfigRequest()
        request_in.set_url(api_in)
        request_in.set_data({"mobile":mobile, "valid": valid})
        response = request_in.post()

        authorization = response.get('token')

        request_out = ConfigRequest()
        request_out.set_url(api_out)
        request_out.set_headers({"Authorization": "Bearer " + authorization})
        response = request_out.get()

        logger.info("Bearer " + authorization)
        logger.info(response)

        self.assertEqual(response.get("code"), 0)