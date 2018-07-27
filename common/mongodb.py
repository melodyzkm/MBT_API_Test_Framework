import get_config
from pymongo import MongoClient

configs = get_config.GetConfig()


class BcfMongo():
    def __init__(self):
        connection = MongoClient(configs.get_servers("BC_MONGODB"), configs.get_servers("PORT_MONGODB"))
        self.db_bcf = connection.bcf
    
    def get_cmc_indicators_with_code(self, code, data_field):
        try:
            return self.db_bcf.token_indicator_slices.find_one({"code": code}).get("indicators").get(data_field)
        except Exception as e:
            print(e)
            return None
    
    def get_twitter_indicators_with_code(self, code, data_field):
        try:
            return self.db_bcf.token_indicator_slices.find_one({"code": code}).get("indicators").get(data_field)
        except Exception as e:
            print(e)
            return None
    
    def get_telegram_indicators_with_code(self, code, data_field):
        try:
            return self.db_bcf.token_indicator_slices.find_one({"code": code}).get("indicators").get(data_field)
        except Exception as e:
            print(e)
            return None
    
    def get_chain_indicators_with_code(self, code, data_field):
        try:
            return self.db_bcf.token_indicator_slices.find_one({"code": code}).get("indicators").get(data_field)
        except Exception as e:
            print(e)
            return None
    
    def get_meta_info_with_code(self, code, data_field):
        valid_fields = ["name", "abbr", "name_cn", "name_en"]
        if data_field in valid_fields:
            try:
                return self.db_bcf.tokens.find_one({"code": code}).get(data_field)
            except Exception as e:
                print(e)
                return None
        else:
            raise ValueError("The key must be {}".format("/".join(valid_fields)))

    def get_user_info(self, mobile):
        try:
            return self.db_bcf.users.find_one({"mobile": mobile})
        except Exception as e:
            print(e)
            return None

    def update(self, table, d_condition, d_update):
        self.db_bcf.get_collection(table).update_one(d_condition, {"$set":d_update})

    def insert(self, table, d_condition, d_update):
        self.db_bcf.get_collection(table).update_one(d_condition, {"$set":d_update})

if __name__  == "__main__":
    m = BcfMongo()
    m.update('users', {"mobile" : "18600000000"}, "a")
