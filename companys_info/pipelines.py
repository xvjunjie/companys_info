# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy import Item
from scrapy.exceptions import DropItem

from utils.log_utils import logger


# class CompanysInfoPipeline(object):
#     def open_spider(self, spider):
#         db_server = spider.settings.get("MONGODB_SERVER", "localhost")
#         # db_port = spider.settings.get("MONGODB_PORT", "27017")
#         db_name = spider.settings.get("MONGODB_DB", "companys_info")
#         db_collection = spider.settings.get("MONGODB_COLLECTION", "companys")
#
#         self.db_client = MongoClient(db_server)
#         self.db = self.db_client[db_name]
#         self.db_collection = self.db[db_collection]
#
#     def close_spider(self, spider):
#         self.db_client.close()
#
#     def process_item(self, item, spider):
#         self.insert_db(item)
#         return item
#
#     def insert_db(self, item):
#         '''
#             插入数据
#         :param item:
#         :return:
#         '''
#         if isinstance(item, Item):
#             item = dict(item)
#
#             valid = True
#             for data in item:
#                 if not data:
#                     valid = False
#                     raise DropItem("Missing {0}!".format(data))
#             if valid:
#                 self.db_collection.insert(item)


class CompanysPipeline(object):
    collection_name = "companys_info"

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_url=crawler.settings.get('MONGODB_SERVER'),
            mongo_db=crawler.settings.get('MONGODB_DB')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logger.debug("Post added to MongoDB")
        return item
