from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Symbol_Flow")
mylog = logfile("Symbol_Flow.log", type=0)


class getSymbolFlow(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        '执行交易对资金流向接口'
        url = url_base + api
        try:
            rep = requests.get(url, timeout=10).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)
        mylog.info(rep)
        self.assertEqual((isinstance(rep, list) and len(rep) > 0), True, msg=rep)


if __name__ == "__main__":
    getSymbolFlow.run()
