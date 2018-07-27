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

class GetQrCode(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_qr_code(self):
        """
        检查返回正确的qr二维码
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

        # get qr code
        api_qr_code = config.get_url("QR_Code")
        token = response_sign_in.get("token")
        headers = {"Authorization": "Bearer {}".format(token)}
        request_qr_code = ConfigRequest()
        request_qr_code.set_headers(headers)
        request_qr_code.set_url(api_qr_code)
        response_qr_code = request_qr_code.get()
        self.assertEqual(len(response_qr_code.get("qr_code")), 2600)
        self.assertEqual(len(response_qr_code.get("invitation")), 6)