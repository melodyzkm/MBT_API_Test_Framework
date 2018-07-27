# -*- coding: UTF-8 -*-
"""
@Version: 1.0
@Project: My Points
@Author: Zhang Kaiming
@Data: 2018/7/23
@Description: 检查手机账户邀请二维码的生成
"""


import time, datetime
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()

log = MyLog.get_log()
logger = log.get_logger()

class ExamineCode(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_examine(self):
        """
        检查返回正确examine结果
        """

        # get login token
        api_login = config.get_url("Login")
        request_sign_in = ConfigRequest()
        data = {"mobile": config.get_login("Mobile"), "valid": config.get_login("Valid")}
        request_sign_in.set_data(data)
        request_sign_in.set_url(api_login)
        response_sign_in = request_sign_in.post()
        self.assertNotEqual(response_sign_in, None)
        self.assertNotEqual(response_sign_in.get("token"), None)

        # get examine result
        api_examine = config.get_url("examine")
        token = response_sign_in.get("token")
        headers = {"Authorization": "Bearer {}".format(token)}
        params_examine = {"type": "examine"}
        params_share = {"type": "share"}

        request_examine = ConfigRequest()
        request_examine.set_headers(headers)
        request_examine.set_params(params_share)
        request_examine.set_url(api_examine)
        response_examine = request_examine.get()
        
        count = response_examine.get("examine_status").get("count")

        # Ur examine count will add 1 time if u share
        request_examine.get()
        request_examine.get()
        response_examine = request_examine.get()
        count += 3
        self.assertEqual(response_examine.get("examine_status").get("count"), count)

        # ur examine count will reduce 1 time if u examine
        for c in range(1, count+1):
            request_examine = ConfigRequest()
            request_examine.set_headers(headers)
            request_examine.set_params(params_examine)
            request_examine.set_url(api_examine)
            response_examine = request_examine.get()
            self.assertEqual(response_examine.get("examine_status").get("count"), count - c)
            self.assertEqual(response_examine.get("hasExamine"), True)

        request_examine = ConfigRequest()
        request_examine.set_headers(headers)
        request_examine.set_params(params_examine)
        request_examine.set_url(api_examine)
        response_examine = request_examine.get()
        self.assertEqual(response_examine.get("examine_status").get("count"), 0)
        self.assertEqual(response_examine.get("hasExamine"), False)
