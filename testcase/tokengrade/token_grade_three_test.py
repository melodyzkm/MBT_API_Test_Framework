# coding=gbk
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Token_Grade")
mylog = logfile("Token_Grade_One.log", type=0)


class tokenGradeThree(TestCase):
    "��ȡ3�����ʱ�"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        'ִ�л�ȡ3�����ʱҽӿ�'
        url = url_base + api
        try:
            rep = requests.get(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep, list) and len(rep)==3), True, msg=rep)


if __name__ == "__main__":
    tokenGradeThree.run()
