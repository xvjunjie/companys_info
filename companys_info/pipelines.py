# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy import Item
from scrapy.exceptions import DropItem

from utils.log_utils import logger


class CompanysPipeline(object):
    # collection_name = "companys_info"

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

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s ' % (data))

        if valid:

            if spider.name == "companys":
                self.db["companys"].insert(dict(item))
                logger.debug("Post added to MongoDB")

            elif spider.name == "p2p_info":
                # self.save_p2p_datas(item)
                if item != None and item["kws_type"] == "positive":

                    result = self.db["positive_info"].find({"title": item["title"]})  # 去重

                    if result.count() != 0:
                        raise DropItem("Duplicate item found: %s" % item)
                    else:

                        self.db["positive_info"].insert(dict(item))
                        logger.debug("positive_info added to MongoDB")

                elif item != None and item["kws_type"] == "negative":

                    title = item["title"]
                    result = self.db["negative_info"].find({"title": title})
                    # print(result)
                    if result.count() != 0:
                        raise DropItem("Duplicate item found: %s" % item)
                    else:
                        self.db["negative_info"].insert(dict(item))
                        logger.debug("negative_info added to MongoDB")
        return item

    def save_p2p_datas(self, item):
        pass
