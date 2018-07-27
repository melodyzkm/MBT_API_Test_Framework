# -*- coding: UTF-8 -*-
"""
@Version: 1.0
@Project: My Points
@Author: Zhang Kaiming
@Data: 2018/7/26
@Description: 检查返回的积分数据
"""

import unittest
import requests
from common.log import MyLog
from get_config import GetConfig
from common.mongodb import BcfMongo
from common.request_data import ConfigRequest

config = GetConfig()

log = MyLog.get_log()
logger = log.get_logger()


class MyPoints(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_points(self):
        """
        检查返回正确用户积分信息
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
        api_my_points = config.get_url("my_points")
        token = response_sign_in.get("token")
        headers = {"Authorization": "Bearer {}".format(token)}

        request = ConfigRequest()
        request.set_headers(headers)
        request.set_url(api_my_points)
        response = request.get()

        # get user infomation from mongodb
        bcf = BcfMongo()
        user_info = bcf.get_user_info(data.get("mobile"))
        self.assertEqual(response.get("mobile"), user_info.get("mobile"))
        self.assertEqual(response.get("invitation"), user_info.get("invitation"))
        self.assertEqual(response.get("point"), user_info.get("point"))
        self.assertEqual(type(response.get("invitationCoun")), int)
        self.assertEqual(type(response.get("effectiveCoun")), int)
        self.assertEqual(type(response.get("invitationScore")), int)
        self.assertEqual(type(response.get("effectctiveScore")), int)
        self.assertEqual(requests.get(response.get("regiserURL")).status_code, 200)
