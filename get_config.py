import yaml
import os
import json
from functools import wraps
cwd_dir_path = os.path.dirname(__file__)
config_file = os.path.join(cwd_dir_path, "config.yaml")


def key_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return result
        else:
            raise AttributeError("attr:{} is not existed".format(args[1:]))
    return wrapper


class GetConfig:
    def __init__(self):
        with open(config_file, "rt") as f:
            contents = f.read()
        self.configs = yaml.load(contents)

    @key_exists
    def get_servers(self, key):
        return self.configs.get("Servers").get(key)

    @key_exists
    def get_url(self, key):
        return self.configs.get("Urls").get(key)

    @key_exists
    def get_login(self, key):
        return self.configs.get("Login").get(key)

    @key_exists
    def get_value(self,*args):
        item=self.configs
        for arg in args:
            item=item.get(arg)
        return item


if __name__ == "__main__":
    c = GetConfig()
    print(c.get_servers("PORT_MONGODB"))
