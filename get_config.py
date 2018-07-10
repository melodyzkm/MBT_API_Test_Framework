import yaml
import os
import json
cwd_dir_path = os.path.dirname(__file__)
config_file = os.path.join(cwd_dir_path, "config.yaml")

class GetConfig:
    def __init__(self):
        with open(config_file, "rt") as f:
            contents = f.read()
        self.configs = yaml.load(contents)

    def get_servers(self, key):
        return self.configs.get("Servers").get(key)

    def get_url(self, key):
        return self.configs.get("Urls").get(key)

    def get_value(self,*args):
        item=self.configs
        for arg in args:
            item=item.get(arg)
            if not item:
                raise AttributeError('attr:%s is not existed'%arg)
        return item


if __name__ == "__main__":
    c = GetConfig()
    print(c.get_value('email','smtp_addr'))
    # print(c.configs)
    # print(c.get_servers("BC_MONGODB"))