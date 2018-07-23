# coding=gbk
"""
@Version: 1.0
@Project: Refreshtoken
@Author: long
@Data: 2018/7/19
@File: Refreshtoken.py
@Description: ��ȡ�ض����������
"""
from unittest import TestCase
import requests
from common.logger import logfile
from get_config import GetConfig

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
login_api = cfg.get_value("Urls", "Login")
api = cfg.get_value("Urls", "refreshtoken")
mylog = logfile("Refreshtoken.log", type=0)
mobile = cfg.get_value("Login", "Mobile")
valid = cfg.get_value("Login", "Valid")


class Refreshtoken(TestCase):
    "ˢ���û���token�͹���ʱ��"

    def setUp(self):
        'ִ��Ԥ������'
        pass

    def tearDown(self):
        pass

    def login(self):
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
        return self.token

    def check(self,token):
        '�ӿ�refreshtoken�ӳ�token��Ч��'
        url = url_base + api
        data = {
            "token": token
        }
        try:
            rep = requests.post(url, data=data).json()
        except Exception as e:
            mylog.critical(e)
            self.assertEqual(True, False, msg=e)

        mylog.info(rep)
        self.assertEqual((isinstance(rep, dict)), True, msg=rep)
        return rep

    def test_correct(self):
        '��ȷִ��ˢ��token�Ľӿ�'
        token = self.login()
        rep = self.check(token)
        self.assertIs(rep.get("code", None), 0, msg="�ӿ�ִ��ʧ��")

        import time
        self.assertAlmostEqual(rep.get("exp"), int(time.time()) + 7 * 24 * 60 * 60, delta=10)

        self.assertIn(len(rep.get('token')), [i for i in range(100, 256)])

    def test_expired(self):
        '�����token�Ѿ�����'
        token = self.login()
        #�ٴ�ִ�е�¼ʹtoken��Ч
        self.login()
        rep = self.check(token)
        self.assertIs(rep.get("code", None), 1, msg="Ԥ�ڷ��ؽ��code=1")

        self.assertIs(rep.get("message", None), "token expired", msg="����msg��Ϣ��Ԥ�ڲ�һ��")


if __name__ == "__main__":
    Refreshtoken.run()
