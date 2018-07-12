# coding=gbk
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
        self.code = '/Bitcoin'
        pass

    def tearDown(self):
        pass

    def test_get(self):
        '执行获取币详情接口'
        url = url_base + api + self.code
        try:
            rep = requests.get(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep, dict)), True, msg=rep)


if __name__ == "__main__":
    tokenGradeOne.run()
