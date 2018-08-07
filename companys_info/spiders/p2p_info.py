# -*- coding: utf-8 -*-
import scrapy

from items import InfoItemLoader, P2pNegativeInfo
from settings import DEFAULT_REQUEST_HEADERS


class P2pInfoSpider(scrapy.Spider):
    name = 'p2p_info'
    allowed_domains = ['wdzj.com']
    start_urls = ['https://www.wdzj.com/news/hangye/']
    negative_kw = ''  # 负面关键字
    positive_kw = ''  # 正面关键字

    def start_requests(self):
        DEFAULT_REQUEST_HEADERS["Referer"] = "https://www.wdzj.com/"
        DEFAULT_REQUEST_HEADERS["Host"] = "www.wdzj.com"

        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_title,
                headers=DEFAULT_REQUEST_HEADERS
            )

    def parse_title(self, response):
        '''
            获取标题
        :return:
        '''
        # title = scrapy.Field()  # 标题
        # summary = scrapy.Field()  # 摘要
        # issuing_time = scrapy.Field()  # 发表时间
        # spider_time = scrapy.Field()  # 爬取时间

        title_li = response.xpath("//div[@class='listbox']//ul[@class='zllist']/li")
        item_local = InfoItemLoader(item=P2pNegativeInfo(), response=response,dont_filter=True)

        for li in title_li:
            title = li.xpath(".//div[@class='text']/h3/a/text()").extract_first().strip()

            with open("negative_kws", "r") as f:
                for kw in f:
                    print(kw + "*" + title)
                    if title.find(kw):
                        item_local.add_value("title", title)
                        item_local.add_xpath("summary", ".//p[@class='cen']/a/text()")
                        item_local.add_xpath("issuing_time", ".//div[@class='lbox']/span[2]/text()")

                        # todo
                        # item_local.load_item("issuing_time",".//div[@class='lbox']/span[2]/text()")#爬取时间

        negative_Info = item_local.load_item()
        yield negative_Info
