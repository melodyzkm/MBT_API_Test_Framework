import yaml
import os

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



# if __name__ == "__main__":
#     c = GetConfig()
#     print(c.get_servers("BC_MONGODB"))