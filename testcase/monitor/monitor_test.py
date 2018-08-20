"""
@Version: 1.0
@Project: Monitor
@Author: long
@Data: 2018/7/27
@File: monitor_test.py
@Description: 交易对资金流向接口
"""
from unittest import TestCase
import requests
from get_config import GetConfig
import time

cfg = GetConfig()
url_base = cfg.get_value("Urls", "Base_Url")
api = cfg.get_value("Urls", "monitor")


class Monitor(TestCase):
    """脱壳关注"""
    id1 = ""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check(self, mid="", limit=20):
        global id1
        url = url_base + api.format(mid, str(limit))
        try:
            rep = requests.get(url, timeout=10).json()
        except Exception as e:
            # mylog.critical(e)
            self.assertEqual(True, False, msg=e)
        # mylog.info(rep)
        self.assertEqual((isinstance(rep, list)), True, msg=rep)
        self.assertIsNot(rep, [], msg="返回结果为空")

        # 判断顺序
        self.assertEqual(rep[-1]["_id"], min([i["_id"] for i in rep]))
        id1 = rep[-1]["_id"]
        for item in rep:
            self.assertIn("event_type", item)
            self.assertIn(item["event_type"], range(1, 10))

            if item.get("event_type") in range(1, 9):

                self.assertIn("_id", item)
                self.assertIn("code", item)
                self.assertIn("time", item)
                self.assertIn("ex_datas", item)

                self.assertEqual(item["ex_datas"], None)
                self.assertGreater(item["cmc_price_usd"], 0)

                self.assertIn("displayCoin", item)
                self.assertIn("_id", item["displayCoin"])
                self.assertIn("code", item["displayCoin"])
                self.assertIn("name", item["displayCoin"])
                self.assertIn("logo_url", item["displayCoin"])
                self.assertIn("name_cn", item["displayCoin"])
                self.assertIn("name_en", item["displayCoin"])
                self.assertIn("name_abbr", item["displayCoin"])

                self.assertIsInstance(item["detail"], list)

                self.assertGreater(min(item["detail"]), 0)

                if item["event_type"] == 8:
                    self.assertGreater(0, item["value"])
                    self.assertGreater(0, item["cmc_change_ratio_24h_usd"])
                elif item["event_type"] == 7:
                    self.assertGreater(item["value"], 0)
                    self.assertGreater(item["cmc_change_ratio_24h_usd"], 0)
                else:
                    self.assertIn("cmc_change_ratio_24h_usd", item)
                    self.assertIn("value", item)

            else:
                self.assertIn("_id", item)
                self.assertIn(item["code"], ["",None])
                self.assertIn("time", item)
                self.assertEqual(item["value"], 0)
                self.assertEqual(item["ex_datas"], ["Bitcoin", "Ethereum", "Litecoin"])

                self.assertIsInstance(item["displayExDatas"], list)
                for subitem in item["displayExDatas"]:
                    self.assertIn("cmc_price_usd", subitem)
                    self.assertIn("cmc_change_ratio_24h_usd", subitem)
                    self.assertIn("displayCoin", subitem)
                    self.assertIn("_id", subitem["displayCoin"])
                    self.assertIn("code", subitem["displayCoin"])
                    self.assertIn("name", subitem["displayCoin"])
                    self.assertIn("logo_url", subitem["displayCoin"])
                    self.assertIn("name_cn", subitem["displayCoin"])
                    self.assertIn("name_en", subitem["displayCoin"])
                    self.assertIn("name_abbr", subitem["displayCoin"])

                    self.assertIsInstance(subitem["detail"], dict)

                    self.assertIn("_id", subitem["detail"])
                    self.assertIn("code", subitem["detail"])
                    self.assertIn(subitem["detail"]["code"], ["Bitcoin", "Ethereum", "Litecoin"])

                    self.assertIn("time", subitem["detail"])
                    self.assertIn("cmc_candle_close", subitem["detail"])
                    self.assertIn("chain_active_user_count_7day", subitem["detail"])
                    self.assertIn("chain_active_user_count_day", subitem["detail"])
                    self.assertIn("chain_new_user_count_7day", subitem["detail"])
                    self.assertIn("chain_new_user_count_day", subitem["detail"])

    def test_001_get(self):
        """首次获取脱壳关注"""
        self.check()

    def test_002_get(self):
        """下拉再次获取脱壳关注"""

        self.check(mid=id1)


if __name__ == "__main__":
    Monitor.run()
