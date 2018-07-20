"""
@Version: 1.0
@Project: Symbol_Flow
@Author: long
@Data: 2018/7/19
@File: Symbol_Flow.py
@Description: 交易对资金流向接口
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig
import time
cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "Symbol_Flow")
mylog = logfile("Symbol_Flow.log", type=0)


class getSymbolFlow(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check(self,market,symbol,cycle,ts):
        '交易对资金流向接口'
        url = url_base + api.format(market,symbol,cycle,ts)
        try:
            rep = requests.get(url, timeout=10).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)
        mylog.info(rep)
        self.assertEqual((isinstance(rep, list)), True, msg=rep)
        for item in rep:
            self.assertIsInstance(item,list)
            self.assertRegex(str(item[0]),r'^1\d{12}$',msg="时间戳错误")
            for i in item[1:10]:
                self.assertGreaterEqual(i,0,msg="数值错误")

    def test_001_get(self):
        '获取币安交易所btc-usdt的资金流向5m周期'
        #获取今日8：00的时间戳
        ts=(int(time.time())//(3600*24))*24*3600*1000
        self.check("binance","btc-usdt","5m","start=%s"%ts)


    def test_002_get(self):
        '获取huobiPro交易所btc-usdt的资金流向1h周期'
        #获取今日8：00的时间戳
        ts=(int(time.time())//(3600*24))*24*3600*1000
        self.check("huobipro","btc-usdt","1h","start=%s"%ts)

    def test_003_get(self):
        '获取okex交易所eth-btc的资金流向1d周期'
        self.check("binance", "btc-usdt", "5m", "last=1")



if __name__ == "__main__":
    getSymbolFlow.run()
