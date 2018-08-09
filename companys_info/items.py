# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re

from datetime import datetime
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose




"""************天眼查**************** """
class InfoItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def filter_monery(value):
    re1 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
    m = rg.search(value)
    if m:
        int1 = m.group(1)
        print(int1)

    return int1

def return_value(value):
    return value


class BusinessInfoItem(scrapy.Item):
    '''工商信息'''
    search_name = scrapy.Field()
    legal_representative = scrapy.Field()  # 法定代表人
    registered_capital = scrapy.Field(
        input_processor=MapCompose(filter_monery),
    )  # 注册资本
    registration_time = scrapy.Field()  # 注册时间
    company_status = scrapy.Field(

    )  # 公司状态
    equity_structure = scrapy.Field()  # 股权结构
    registration_number = scrapy.Field()  # 工商注册号
    credit_code = scrapy.Field()  # 统一信用代码
    agency_code = scrapy.Field()  # 组织机构代码
    type_of_company = scrapy.Field()  # 公司类型
    identification_number = scrapy.Field()  # 纳税人识别号
    industry = scrapy.Field()  # 行业
    operating_period = scrapy.Field()  # 营业期限
    approval_date = scrapy.Field()  # 核准日期
    registration_authority = scrapy.Field()  # 登记机关
    english_name = scrapy.Field()  # 英文名称
    registered_address = scrapy.Field()  # 注册地址
    business_scope = scrapy.Field()  # 经营范围


class CompanysInfoItem(scrapy.Item):
    detail_url = scrapy.Field()



"""************p2p网贷**************** """

def filter_title(value):
    '''查找title是否有某一个关键字'''

    title = value.strip()

    with open("negative_kws", "r") as f:
        for kw in f:
            print(kw)
            if kw in title:
                print(title)
                return title

def date_convert(value):
    try:
        create_date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        create_date = datetime.now()
        # date = datetime.strptime(create_date, '%Y-%m-%d %H:%M:%S')


    return create_date




class P2pInfo(scrapy.Item):
    kws_type = scrapy.Field()#关键词类型，0负面，1正面
    title = scrapy.Field(
        # input_processor=MapCompose(filter_title)
    )#标题
    summary = scrapy.Field()#摘要
    issuing_time = scrapy.Field(
        input_processor = MapCompose(date_convert)
    )#发表时间
    spider_time = scrapy.Field(

    )#爬取时间
    content = scrapy.Field()#详情的内容
