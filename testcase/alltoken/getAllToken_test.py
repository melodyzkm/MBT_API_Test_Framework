"""
@Version: 1.0
@Project: Get_Token_All
@Author: long
@Data: 2018/7/19
@File: Get_Token_All.py
@Description: 获取token列表接口
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Get_Token_All")
# mylog = logfile("Get_Token_All.log", type=0)


class GetAllToken(TestCase):
    """获取token列表"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        """执行获取token列表接口"""
        url = url_base + api
        try:
            rep = requests.get(url).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)
        # mylog.info(rep)
        self.assertEqual((isinstance(rep, list) and len(rep) > 0), True, msg=rep)

        for item in rep:
            self.assertIsInstance(item.get("_id", None), str)
            self.assertIsNot(item.get("_id", None), "")

            self.assertIsInstance(item.get("code", None), str)
            self.assertIsNot(item.get("code", None), "")

            self.assertIsInstance(item.get("name", None), str)
            # self.assertIsNot(item.get("name", None), "")

            # self.assertIsInstance(item.get("logo_url", None), str)
            if item.get("logo_url", None):
                self.assertRegex(item.get("logo_url", None), r'^http')

            # self.assertIsInstance(item.get("name_cn", None), str)
            if "name_cn" in item and item.get("name_cn"):
                self.assertRegex(item.get("name_cn", None), r'[\u2E80-\u9FFF]+')

            self.assertIsInstance(item.get("name_abbr", None), str)

            self.assertIsInstance(item.get("name_en", None), str)
            if item.get("name_abbr", None):
                self.assertRegex(item.get("name_abbr", None), r'[^\u2E80-\u9FFF]+')


if __name__ == "__main__":
    GetAllToken.run()
