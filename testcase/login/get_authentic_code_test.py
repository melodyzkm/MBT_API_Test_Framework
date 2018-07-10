"""
@Version: 1.0
@Project: LoginTest
@Author: Kevin Chang
@Data: 2018/7/9
@File: get_authentic_code_test.py
@Description: 检查获取验证码的接口
"""


import random
import os
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()
base_url = config.get_url("Base_Url")
valid_api = "/api/v3/valid"

log = MyLog.get_log()
logger = log.get_logger()

class GetAuthenticCode(unittest.TestCase):

    def setUp(self):
        print("Test start")

    def tearDown(self):
        print("Test end")

    def test_send(self):
        """
        检查可以正确发送验证码
        """

        cellphone = "186" +  ''.join([ str(i) for i in random.sample(range(10),8)])
        request = ConfigRequest()
        request.set_url(valid_api)
        request.set_data({"mobile":cellphone})
        response = request.post()

        self.assertEqual(response.get("code"), 0)


    def test_send_again(self):
        """
        检查同一手机号无法连续发送验证码
        """

        cellphone = "186" + ''.join([str(i) for i in random.sample(range(10), 8)])
        request = ConfigRequest()
        request.set_url(valid_api)
        request.set_data({"mobile":cellphone})
        request.post()
        response = request.post()

        self.assertNotEqual(response.get("code"), 0)


    def test_invalid_cellphone_no(self):
        """
        非法手机号无法发送验证码
        """
        cellphone = "186" +  ''.join([ str(i) for i in random.sample(range(10),7)])
        request = ConfigRequest()
        request.set_url(valid_api)
        request.set_data({"mobile":cellphone})
        response = request.post()

        logger.info(response)
        self.assertNotEqual(response.get("code"), 0)