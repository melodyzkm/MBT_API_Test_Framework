
"""
@Version: 1.0
@Project: Capital Flow
@Author: Kevin Chang
@Data: 2018/7/9
@File: token_capital_flow.py
@Description: 检查资金流向
"""


import random
import unittest
from common.log import MyLog
from get_config import GetConfig
from common.request_data import ConfigRequest

config = GetConfig()
base_url = config.get_url("Base_Url")
flow_api = "/api/v2/tokens/flow/1d"

log = MyLog.get_log()
logger = log.get_logger()
logger.info("{} start".format(__file__))

class GetAuthenticCode(unittest.TestCase):

    def test_send(self):
        """
            检查可以正确发送验证码
        """

        cellphone = "186" +  ''.join([ str(i) for i in random.sample(range(10),8)])
        post = ConfigRequest()
        post.set_url(valid_api)
        post.set_data({"mobile":cellphone})
        response = post.post()

        self.assertEqual(response.get("code"), 0)


    def test_send_again(self):
        """
            检查同一手机号无法连续发送验证码
        """

        cellphone = "186" + ''.join([str(i) for i in random.sample(range(10), 8)])
        post = ConfigRequest()
        post.set_url(valid_api)
        post.set_data({"mobile":cellphone})
        post.post()
        response = post.post()

        self.assertNotEqual(response.get("code"), 0)


    def test_invalid_cellphone_no(self):
        """
        非法手机号无法发送验证码
        """
        cellphone = "186" +  ''.join([ str(i) for i in random.sample(range(10),7)])
        post = ConfigRequest()
        post.set_url(valid_api)
        post.set_data({"mobile":cellphone})
        response = post.post()

        logger.info(response)
        self.assertNotEqual(response.get("code"), 0)