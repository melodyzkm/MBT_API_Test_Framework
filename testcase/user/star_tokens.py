# coding=gbk
"""
@Version: 1.0
@Project: StarTokens
@Author: long
@Data: 2018/7/23
@File: StarTokens.py
@Description: ��ȡ�ض����������
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig
import json

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
login_api = cfg.get_value("Urls", "Login")
api = cfg.get_value("Urls", "star_tokens")
# mylog = logfile("star_tokens.log", type=0)
mobile = cfg.get_value("Login", "Mobile")
valid = cfg.get_value("Login", "Valid")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}


class StarTokens(TestCase):
    """��ȡ�û�����ѡ��/���׶�"""

    def setUp(self):
        'ִ��Ԥ������'
        url = url_base + login_api
        data = {
            "mobile": mobile,
            "valid": valid
        }
        try:
            rep = requests.post(url, data=data).json()
            self.assertIs(rep.get("code", None), 0, msg="��¼ʧ��")
            self.token = rep.get("token", None)
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

    def tearDown(self):
        pass

    def get_startokens(self):
        '��ȡ��ѡ��'
        url = url_base + api + "?token=" + self.token
        try:
            rep = requests.get(url).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        return rep

    def post_startokens(self, type, value, market=None):
        '�����ѡ��'
        url = url_base + api + "?token=" + self.token
        if not market:
            data = {
                "stars": [
                    {
                        "type": type,
                        "code": value
                    }
                ]
            }
        else:
            data = {
                "stars": [
                    {
                        "type": type, "market": market, "symbol": value
                    }
                ]
            }
        try:
            rep = requests.post(url, json=data, headers=header).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        # mylog.info(rep)

    def delete_startokens(self, type, value, market=None):
        'ɾ����ѡ��'
        url = url_base + api + "?token=" + self.token
        if not market:
            data = {
                "stars": [
                    {
                        "type": type, "code": value
                    }
                ]
            }
        else:
            data = {
                "stars": [
                    {
                        "type": type, "market": market, "symbol": value
                    }
                ]
            }
        try:
            rep = requests.delete(url, json=data).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        # mylog.info(rep)

    def put_startokens(self, data):
        '������ѡ��'
        url = url_base + api + "?token=" + self.token
        try:
            rep = requests.put(url, json=data).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        # mylog.info(rep)

    def test_all(self):
        """��->��->����->��->ɾ->��"""
        "���������Һ�һ�����׶�"
        self.post_startokens("token", "Bitcoin")
        self.post_startokens("token", "0x8f8221afbb33998d8584a2b05749ba73c37a938a")
        self.post_startokens("symbol", "eth-btc", market="huobipro")

        "��ȡ��ѡ��/���׶�"
        rep = self.get_startokens()
        self.assertIs(rep.get("code", None), 0, msg="�ӿ�ִ��ʧ��")

        self.assertIn("results", rep)

        self.assertIn("Bitcoin", [i.get("code") for i in rep.get("results")])
        self.assertIn("0x8f8221afbb33998d8584a2b05749ba73c37a938a", [i.get("code") for i in rep.get("results")])
        self.assertIn("eth-btc", [i.get("symbol") for i in rep.get("results")])

        for item in rep.get("results"):
            if "market" in item:
                self.assertIn("symbol", item)
                self.assertIn("open", item)
                self.assertIn("close", item)
                self.assertIn("high", item)
                self.assertIn("low", item)
                self.assertIn("volume", item)
                self.assertIn("amount", item)
                self.assertIn("change", item)
                self.assertIn("change_ratio", item)
                self.assertIn("type", item)
                self.assertIn("market_name_cn", item)
                self.assertIn("market_name_en", item)
                self.assertIn("take_code", item)
                self.assertIn("pay_code", item)
                self.assertIn("code", item)
                self.assertIn("name", item)
                self.assertIn("name_cn", item)
                self.assertIn("name_en", item)
                self.assertIn("name_abbr", item)
                self.assertIn("price", item)
            else:
                self.assertIn("code", item)
                self.assertIn("name", item)
                self.assertIn("name_cn", item)
                self.assertIn("name_en", item)
                self.assertIn("name_abbr", item)
                self.assertIn("logo_url", item)
                self.assertIn("price", item)
                self.assertIn("change_ratio", item)
                self.assertIn("change", item)
                self.assertIn("change_ratio_1h", item)
                self.assertIn("change_1h", item)
                self.assertIn("change_ratio_7d", item)
                self.assertIn("change_7d", item)
                self.assertIn("type", item)

        "����˳��"
        data = {"stars": [{"type": "symbol", "market": "huobipro", "symbol": "eth-btc"},
                          {"type": "token", "code": "Bitcoin"},
                          {"type": "token", "code": "0x8f8221afbb33998d8584a2b05749ba73c37a938a"}]}

        self.put_startokens(data)
        "��ȡ��ѡ��/���׶�"
        rep = self.get_startokens()
        self.assertEqual("eth-btc",rep["results"][0]["symbol"])
        self.assertEqual("Bitcoin",rep["results"][1]["code"])
        self.assertEqual("0x8f8221afbb33998d8584a2b05749ba73c37a938a",rep["results"][2]["code"])

        "ɾ����ѡ��"
        self.delete_startokens("token", "Bitcoin")
        self.delete_startokens("token", "0x8f8221afbb33998d8584a2b05749ba73c37a938a")
        rep = self.get_startokens()
        self.assertNotIn("Bitcoin", [i.get("code") for i in rep.get("results")])
        self.assertNotIn("0x8f8221afbb33998d8584a2b05749ba73c37a938a", [i.get("code") for i in rep.get("results")])
        self.assertIn("eth-btc", [i.get("symbol") for i in rep.get("results")])
        "ɾ����ѡ���׶�"
        self.delete_startokens("symbol", "eth-btc", market="huobipro")
        rep = self.get_startokens()
        self.assertNotIn("Bitcoin", [i.get("code") for i in rep.get("results")])
        self.assertNotIn("0x8f8221afbb33998d8584a2b05749ba73c37a938a", [i.get("code") for i in rep.get("results")])
        self.assertNotIn("eth-btc", [i.get("symbol") for i in rep.get("results")])

if __name__ == "__main__":
    StarTokens.run()
