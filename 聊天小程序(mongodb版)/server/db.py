import pymongo
from config import *


class MyMongoDB:
    def __init__(self,database,collection):
        # 建立链接
        self.client = pymongo.MongoClient(DB_HOST,DB_PORT)
        # 指定数据库
        self.db = self.client[database]
        # 指定集合
        self.collection = self.db[collection]
        
    # insert_one ,insert_many
    def insert(self,*data):
        # 是一个元组
        # print(data)
        if len(data) == 1:
            # 取元组的第一个值
            # 插入的是字典
            self.collection.insert_one(data[0])
        else:
            # 元组要转换成列表
            # 插入的是一个列表里面包含的字典
            self.collection.insert_many(list(data))
            
    # update_one, update_many
    def update(self,data,new_data,m = False):
        if m:
            self.collection.update_many(data, {'$set': new_data})
        else:
            self.collection.update_one(data,{'$set':new_data})

    # delete_one,delete_many
    def delete(self,data,m = False):
        if m:
            self.collection.delete_many(data)
        else:
            self.collection.delete_one(data)

    # find_one,find
    def find(self,data={},m=False):
        if m:
            result=self.collection.find(data)
            return result
        else:
            result = self.collection.find_one(data)
            return result

