# coding=gbk
"""
@Version: 1.0
@Project: Token_Grade_One
@Author: long
@Data: 2018/7/19
@File: Token_Grade_One.py
@Description: 获取特定币体检详情
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Token_Grade")
mylog = logfile("Token_Grade_One.log", type=0)


class tokenGradeOne(TestCase):
    "获取币体检详情"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check(self, code):
        '执行获取币详情接口'
        url = url_base + api + "/" + code
        try:
            rep = requests.get(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep, dict)), True, msg=rep)

        self.assertIsInstance(rep.get("_id", None), str)
        self.assertIsNot(rep.get("_id", None), "")

        self.assertEqual(rep.get("code", None), code)

        self.assertIsInstance(rep.get("indicators", None), dict)

        self.assertIsInstance(rep.get("name", None), str)
        self.assertIsNot(rep.get("name", None), "")

        if rep.get("logo_url", None):
            self.assertRegex(rep.get("logo_url", None), r'^http')

        if rep.get("name_cn", None):
            self.assertRegex(rep.get("name_cn", None), r'[\u2E80-\u9FFF]+')

        self.assertIsInstance(rep.get("name_abbr", None), str)

        self.assertIsInstance(rep.get("name_en", None), str)
        if rep.get("name_abbr", None):
            self.assertRegex(rep.get("name_abbr", None), r'[^\u2E80-\u9FFF]+')

        self.assertIsInstance(rep.get("_id", None), str)
        self.assertIsNot(rep.get("_id", None), "")

        if rep.get("chain_user_count_score", None):
            self.assertIsInstance(rep.get("chain_user_count_score", None), int)
            self.assertGreaterEqual(rep.get("chain_user_count_score"),0)
            self.assertGreaterEqual(100,rep.get("chain_user_count_score"))

            self.assertIsInstance(rep.get("chain_user_count_value", None), int)

            self.assertIn(rep.get("chain_user_count_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("chain_user_count_score_text", None), str)

        if rep.get("chain_active_user_count_5day_score", None):
            self.assertIsInstance(rep.get("chain_active_user_count_5day_score", None), int)
            self.assertGreaterEqual(rep.get("chain_active_user_count_5day_score"),0)
            self.assertGreaterEqual(100,rep.get("chain_active_user_count_5day_score"))

            self.assertIsInstance(rep.get("chain_active_user_count_5day_value", None), int)

            self.assertIn(rep.get("chain_active_user_count_5day_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("chain_active_user_count_5day_score_text", None), str)

        if rep.get("twitter_follower_count_score", None):
            self.assertIsInstance(rep.get("twitter_follower_count_score", None), int)
            self.assertGreaterEqual(rep.get("twitter_follower_count_score"),0)
            self.assertGreaterEqual(100,rep.get("chain_user_count_score"))

            self.assertIsInstance(rep.get("twitter_follower_count_value", None), int)

            self.assertIn(rep.get("twitter_follower_count_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("twitter_follower_count_score_text", None), str)

        if rep.get("twitter_follower_count_7day_score", None):
            self.assertIsInstance(rep.get("twitter_follower_count_7day_score", None), int)
            self.assertGreaterEqual(rep.get("twitter_follower_count_7day_score"),0)
            self.assertGreaterEqual(100,rep.get("twitter_follower_count_7day_score"))

            self.assertIsInstance(rep.get("twitter_follower_count_7day_value", None), int)

            self.assertIn(rep.get("twitter_follower_count_7day_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("twitter_follower_count_7day_score_text", None), str)

        if rep.get("telegram_user_count_score", None):
            self.assertIsInstance(rep.get("telegram_user_count_score", None), int)
            self.assertGreaterEqual(rep.get("telegram_user_count_score"),0)
            self.assertGreaterEqual(100,rep.get("telegram_user_count_score"))

            self.assertIsInstance(rep.get("telegram_user_count_value", None), int)

            self.assertIn(rep.get("telegram_user_count_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("telegram_user_count_score_text", None), str)

        if rep.get("telegram_user_count_7day_score", None):
            self.assertIsInstance(rep.get("telegram_user_count_7day_score", None), int)
            self.assertGreaterEqual(rep.get("telegram_user_count_7day_score"),0)
            self.assertGreaterEqual(100,rep.get("telegram_user_count_7day_score"))

            self.assertIsInstance(rep.get("telegram_user_count_7day_value", None), int)

            self.assertIn(rep.get("telegram_user_count_7day_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("telegram_user_count_7day_score_text", None), str)

        if rep.get("git_commit_count_score", None):
            self.assertIsInstance(rep.get("git_commit_count_score", None), int)
            self.assertGreaterEqual(rep.get("git_commit_count_score"),0)
            self.assertGreaterEqual(100,rep.get("git_commit_count_score"))

            self.assertIsInstance(rep.get("git_commit_count_value", None), int)

            self.assertIn(rep.get("git_commit_count_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("git_commit_count_score_text", None), str)

        if rep.get("git_commit_count_30day_score", None):
            self.assertIsInstance(rep.get("git_commit_count_30day_score", None), int)
            self.assertGreaterEqual(rep.get("git_commit_count_30day_score"),0)
            self.assertGreaterEqual(100,rep.get("git_commit_count_30day_score"))

            self.assertIsInstance(rep.get("git_commit_count_30day_value", None), int)

            self.assertIn(rep.get("git_commit_count_30day_score_level", None),["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","E"] )

            self.assertIsInstance(rep.get("git_commit_count_30day_score_text", None), str)

        self.assertIsInstance(rep.get("chain_avg_value", None), (float,int,))
        self.assertIsInstance(rep.get("community_avg_value", None), (float,int,))
        self.assertIsInstance(rep.get("code_avg_value", None), (float,int,))
        self.assertIsInstance(rep.get("chain_avg_score", None), (float,int,))
        self.assertIsInstance(rep.get("community_avg_score", None), (float,int,))
        self.assertIsInstance(rep.get("code_avg_score", None), (float,int,))
        self.assertIsInstance(rep.get("general_score", None), (float,int,))
        self.assertIn(rep.get("chain_avg_score_level", None),
                      ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])
        self.assertIn(rep.get("community_avg_score_level", None),
                      ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])
        self.assertIn(rep.get("code_avg_score_level", None),
                      ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])
        self.assertIn(rep.get("general_score_level", None),
                      ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])
        self.assertIsInstance(rep.get("general_score_text", None), str)
        self.assertIsNot(rep.get("general_score_text", None), "")

    def test_001_get(self):
        '比特币体检'
        self.check("Bitcoin")

    def test_002_get(self):
        'REQ体检'
        self.check("0x8f8221afbb33998d8584a2b05749ba73c37a938a")
if __name__ == "__main__":
    tokenGradeOne.run()
