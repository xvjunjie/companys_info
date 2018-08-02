# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class CompanysInfoItem(scrapy.Item):
    pass


class BusinessInfoItemLoader(ItemLoader):
    default_output_processor = TakeFirst


def filter_monery(value):
    re1 = '(\\d+)'  # Integer Number 1

    rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
    m = rg.search(value)
    if m:
        int1 = m.group(1)
        print(int1)

    return int1


class BusinessInfoItem(scrapy.Item):
    '''工商信息'''
    search_name = scrapy.Field()
    legal_representative = scrapy.Field()  # 法定代表人
    registered_capital = scrapy.Field(
        input_processor=MapCompose(filter_monery),
    )  # 注册资本
    registration_time = scrapy.Field()  # 注册时间
    company_status = scrapy.Field()  # 公司状态
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
