from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Get_Token_All")
mylog=logfile("Get_Token_All.log",type=0)

class getAllToken(TestCase):
    "获取token列表"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        '执行获取token列表接口'
        url = url_base + api
        try:
            rep=requests.get(url).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True,False,msg=e)
        mylog.info(rep)
        self.assertEqual((isinstance(rep,list) and len(rep)>0),True,msg=rep)

if __name__=="__main__":
    getAllToken.run()

