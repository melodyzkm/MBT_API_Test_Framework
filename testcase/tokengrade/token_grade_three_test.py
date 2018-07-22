# coding=gbk
"""
@Version: 1.0
@Project: Token_Grade_One
@Author: long
@Data: 2018/7/19
@File: Token_Grade_One.py
@Description: 获取推荐币体检详情
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Token_Grade")
mylog = logfile("Token_Grade_One.log", type=0)


class TokenGradeThree(TestCase):
    "获取3个优质币"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        '执行获取3个优质币接口'
        url = url_base + api
        try:
            rep = requests.get(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep, list) and len(rep)==3), True, msg=rep)
        for item in rep:
            self.assertIsInstance(item.get("_id", None), str)
            self.assertIsNot(item.get("_id", None), "")

            self.assertIsInstance(item.get("code", None), str)

            self.assertIsInstance(item.get("indicators", None), dict)

            self.assertIsInstance(item.get("name", None), str)
            self.assertIsNot(item.get("name", None), "")

            if item.get("logo_url", None):
                self.assertRegex(item.get("logo_url", None), r'^http')

            if item.get("name_cn", None):
                self.assertRegex(item.get("name_cn", None), r'[\u2E80-\u9FFF]+')

            self.assertIsInstance(item.get("name_abbr", None), str)

            self.assertIsInstance(item.get("name_en", None), str)
            if item.get("name_abbr", None):
                self.assertRegex(item.get("name_abbr", None), r'[^\u2E80-\u9FFF]+')

            self.assertIsInstance(item.get("_id", None), str)
            self.assertIsNot(item.get("_id", None), "")

            if item.get("chain_user_count_score", None):
                self.assertIsInstance(item.get("chain_user_count_score", None), int)
                self.assertGreaterEqual(item.get("chain_user_count_score"), 0)
                self.assertGreaterEqual(100, item.get("chain_user_count_score"))

                self.assertIsInstance(item.get("chain_user_count_value", None), int)

                self.assertIn(item.get("chain_user_count_score_level", None),
                              ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])

                self.assertIsInstance(item.get("chain_user_count_score_text", None), str)

            if item.get("chain_active_user_count_5day_score", None):
                self.assertIsInstance(item.get("chain_active_user_count_5day_score", None), int)
                self.assertGreaterEqual(item.get("chain_active_user_count_5day_score"), 0)
                self.assertGreaterEqual(100, item.get("chain_active_user_count_5day_score"))

                self.assertIsInstance(item.get("chain_active_user_count_5day_value", None), int)

                self.assertIn(item.get("chain_active_user_count_5day_score_level", None),
                              ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])

                self.assertIsInstance(item.get("chain_active_user_count_5day_score_text", None), str)


if __name__ == "__main__":
    TokenGradeThree.run()
