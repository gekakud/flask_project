from pymongo import MongoClient
import common


class MongoDbWrapper:

    def is_config_exist(self, config_key):
        return self.configs_collection.count_documents({'key': config_key}) > 0

    def insert_new_config(self, config):
        if self.is_config_exist(config_key=config['key']):
            raise Exception("Item with key " + config.key + " already exist!")

        return self.configs_collection.insert_one(config)

    def update_config_value(self, config):
        if not self.is_config_exist(config_key=config['key']):
            raise Exception("Cannot update item with key " + config.key + " - it doesn't exist!")

        query = {'key':config['key']}
        newvalues = {"$set": {'value':config['value']}}
        self.configs_collection.update_one(query, newvalues)

    def delete_config(self, config_key):
        query = {'key':config_key}
        self.configs_collection.delete_one(query)

    def get_all_configs(self):
        return self.configs_collection.find({})

    def get_config_by_key(self, config_key):
        # exclude _id
        xx = self.configs_collection.find_one({'key': config_key}, {'_id' : 0})
        return xx

    def configs_count(self):
        return self.configs_collection.count_documents(filter={})

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client.get_database('demo_configs_db')
        if self.db.list_collection_names().count("ConfigsCollection") == 0:
            self.db.create_collection("ConfigsCollection")

        if self.db.list_collection_names().count("FwImagesCollection") == 0:
            self.db.create_collection("FwImagesCollection")

        self.configs_collection = self.db.get_collection('ConfigsCollection')
        self.fm_collection = self.db.get_collection('FwImagesCollection')


mongo_client = MongoDbWrapper(common.mongodb_connection_string)
# print(str(mongo_client.configs_count()))
# # ff = mongo_client.insert_new_config({'key':'ee', 'value':'hhhh'})
# tt = mongo_client.is_config_exist('ggg')
# mongo_client.update_config_value({'key':'aa', 'value':'uraaaa'})
# mongo_client.delete_config('ggg')
# rr = mongo_client.get_config_by_key('aa')
# bb = mongo_client.get_all_configs()
# for x in bb:
#     print(x)
# print("ok")
