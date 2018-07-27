# -*- coding: UTF-8 -*-
"""
@Version: 1.0
@Project: My Points
@Author: Zhang Kaiming
@Data: 2018/7/29
@Description: 检查积分管理接口
"""

import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest
from common.mongodb import BcfMongo

config = GetConfig()

log = MyLog.get_log()
logger = log.get_logger()

class PointsManagement(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_points_management(self):
        """
        检查积分管理接口
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

        d_type_enum = {
            'register': 0,
            'bindWeChat': 888,  # 绑定we Chat
            'invitation': 2000,  # 邀请用户积分
            'effective': 2000,  # 有效用户积分
            'shareNews': 80,  # 分享积分
            'shareFocus': 80,  # 分享脱壳关注
            'shareCoin': 80,  # 分享币体检
            'shareWeChat': 80,  # 微信 qq二维码 链接分享 分享统一的注册地址
            'shareToken': 80,  # 币种分享
            'shareMarket': 80,  # 交易对分享
        }

        api_points_management = config.get_url("points_management")
        token = response_sign_in.get("token")
        headers = {"Authorization": "Bearer {}".format(token)}

        for type_get_point in d_type_enum:
            self.reset_point_and_point_status_shared_count()
            request_share = ConfigRequest()
            request_share.set_url(api_points_management)
            request_share.set_headers(headers)
            request_share.set_data({"type": type_get_point})
            response = request_share.post()
            self.assertEqual(response.get("data").get("point"), d_type_enum.get(type_get_point))
            self.assertEqual(response.get("data").get("point_status_shared").get("count"), 1)


    def reset_point_and_point_status_shared_count(self):
        mobile = config.get_login("Mobile")
        db_bcf = BcfMongo()
        user_info = db_bcf.get_user_info(mobile)
        if user_info.get("point") > 0:
            db_bcf.update("users", {"mobile": mobile}, {"point": 0})
        if user_info.get("point_status_shared").get("count") > 0:
            db_bcf.update("users", {"mobile": mobile}, {"point_status_shared.count": 0})

