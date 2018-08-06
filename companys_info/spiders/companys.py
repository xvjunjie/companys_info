# -*- coding: utf-8 -*-
import urllib

import scrapy

from items import BusinessInfoItem, BusinessInfoItemLoader, CompanysInfoItem
from settings import DEFAULT_REQUEST_HEADERS, headers2
from utils.log_utils import logger


class CompanysSpider(scrapy.Spider):
    name = "companys"
    allowed_domains = ["tianyancha.com"]
    start_urls = (
        'http://www.tianyancha.com/',
    )

    company_name = ''
    new_url = None
    url = None

    def start_requests(self):
        with open("company_list", "r") as f:
            for obj in f:
                DEFAULT_REQUEST_HEADERS["Referer"] = "https://www.tianyancha.com/"
                self.company_name = obj
                print(self.company_name.split())
                # businessinfo_item = BusinessInfoItem()
                # businessinfo_item["search_name"] = self.company_name.split()

                self.url = "http://www.tianyancha.com/search?key=%s" % (urllib.parse.quote(self.company_name))
                yield scrapy.Request(self.url, headers=DEFAULT_REQUEST_HEADERS,
                                     callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        headers2["Referer"] = self.url

        detail_url = response.xpath("//*[@id='web-content']/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/a/@href").extract_first()



        # item_local = BusinessInfoItemLoader(item=CompanysInfoItem(), response=response)
        # item_local.add_xpath()
        # companys_info_item = item_local.load_item()
        # yield companys_info_item

        if detail_url:
            # parse_url = detail_url.encode('utf-8')
            DEFAULT_REQUEST_HEADERS["Referer"] = detail_url
            yield scrapy.Request(
                url=detail_url,
                headers=DEFAULT_REQUEST_HEADERS,
                callback=self.parse_detail

            )


    def parse_detail(self, response):
        # businessinfo_item = BusinessInfoItem()
        item_local = BusinessInfoItemLoader(item=BusinessInfoItem(), response=response)

        # search_name = scrapy.Field()
        # legal_representative = scrapy.Field()  # 法定代表人
        # registered_capital = scrapy.Field()  # 注册资本
        # registration_time = scrapy.Field()  # 注册时间
        # company_status = scrapy.Field()  # 公司状态
        # equity_structure = scrapy.Field()  # 股权结构，要开通
        # registration_number = scrapy.Field()  # 工商注册号
        # credit_code = scrapy.Field()  # 统一信用代码
        # agency_code = scrapy.Field()  # 组织机构代码
        # type_of_company = scrapy.Field()  # 公司类型
        # identification_number = scrapy.Field()  # 纳税人识别号
        # industry = scrapy.Field()  # 行业
        # operating_period = scrapy.Field()  # 营业期限
        # approval_date = scrapy.Field()  # 核准日期
        # registration_authority = scrapy.Field()  # 登记机关
        # english_name = scrapy.Field()  # 英文名称
        # registered_address = scrapy.Field()  # 注册地址
        # business_scope = scrapy.Field()  # 经营范围

        # 规则
        item_local.add_xpath("legal_representative", "//div[@class='humancompany']//a/text()")
        item_local.add_xpath("registered_capital", "//table[@class='table']//tr[1]/td[2]/div[2]/@title")


        #todo
        item_local.add_xpath("registration_time",
                             "//*[@id='_container_baseInfo']/table[1]/tbody/tr[2]/td/div[2]/text()")  # js要改
        item_local.add_xpath("company_status", "//div[@class='num-opening']/text()")
        # item_local.add_xpath("equity_structure", "//div[@class='num-opening']/text()")# 股权结构，要开通
        item_local.add_xpath("registration_number",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[1]/td[2]/text()")
        item_local.add_xpath("credit_code",
                             "//*[@id='_container_baseInfo']/table[2]/tbody/tr[2]/td[2]/text()")
        item_local.add_xpath("agency_code",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[1]/td[4]/text()")
        item_local.add_xpath("type_of_company",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[2]/td[4]/text()")
        # item_local.add_xpath("identification_number", "") #跟纳税人识别号一样
        item_local.add_xpath("industry",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[3]/td[4]/text()")
        item_local.add_xpath("operating_period",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[4]/td[2]/span/text()")

        #todo
        item_local.add_xpath("approval_date",
                             "//table[@class='table -striped-col -border-top-none']/tbody/tr[4]/td[4]/text/text()")  # js要该
        item_local.add_xpath("registration_authority", "//*[@id='_container_baseInfo']/table[2]/tbody/tr[6]/td[4]/text()")
        # item_local.add_xpath("english_name", "")
        item_local.add_xpath("registered_address", "//*[@id='_container_baseInfo']/table[2]/tbody/tr[8]/td[2]/text()")
        item_local.add_xpath("business_scope", "//span[@class='js-split-container']/text()")

        businessinfo_item = item_local.load_item()

        yield businessinfo_item
