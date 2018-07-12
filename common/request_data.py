import requests
import get_config
from common.log import MyLog as Log

configs = get_config.GetConfig()


class ConfigRequest:
    def __init__(self):
        global base_url, timeout
        base_url = configs.get_url("Base_Url")
        timeout = configs.get_url("Time_Out")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.params = {}
        self.headers = {}
        self.data = {}

    def set_url(self, post_url):
        self.url = base_url + post_url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, parameters):
        self.params = parameters

    def set_data(self, data):
        self.data = data

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=timeout)
            return  response.json()
        except TimeoutError:
            self.logger.error("Time out: {}".format(self.url))
            return None

    def post(self):
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers, timeout=timeout)
            return  response.json()
        except TimeoutError:
            self.logger.error("Time out: {}".format(self.url))
            return  None

if __name__ == "__main__":
    c = ConfigRequest()
    c.set_url("/api/v1/home/market_cap_ratio")
    print(c.get())

