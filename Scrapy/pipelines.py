# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import pprint
class ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item




class LagouPipline(object):

    def __init__(self):
        self.conn = MongoClient('localhost', 27017)
        self.db = self.conn.local
        self.set = self.db.lagou

    def process_item(self, item, spider):
        print('数据库操作')
        print(item)
        postion_info = self.set.find_one({'positionId': item['positionId']})
        if postion_info:
            self.set.update({'positionId': item['positionId']}, {'$set': dict(item)})
        else:
            insert_result = self.set.insert(dict(item))

        return item

