# -*- coding: utf-8 -*-
import urllib

import scrapy

from items import InfoItemLoader, P2pInfo
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
        p2pInfo1 = P2pInfo()
        p2pInfo2 = P2pInfo()

        negative_item = InfoItemLoader(item=p2pInfo1, response=response, dont_filter=True)
        positive_item = InfoItemLoader(item=p2pInfo2, response=response, dont_filter=True)

        for li in title_li:
            title = li.xpath(".//div[@class='text']/h3/a/text()").extract_first().strip()

            with open("negative_kws", "r") as negative_kws:
                for negative in negative_kws:
                    is_title = title.find(negative.strip())
                    if is_title != -1:
                        negative_item.add_value("kws_type", "negative")
                        negative_item.add_value("title", title)
                        negative_item.add_xpath("summary", ".//p[@class='cen']/a/text()")
                        negative_item.add_xpath("issuing_time", ".//div[@class='lbox']/span[2]/text()")

                        detail_url = li.xpath("./div[2]/h3/a/@href").extract_first()

                        yield scrapy.Request(
                            url=urllib.parse.urljoin(response.url, detail_url),
                            callback=self.parse_detail,
                            meta={"negative_item": negative_item},
                            headers=DEFAULT_REQUEST_HEADERS
                        )

            with open("positive_kws", "r") as positive_kws:
                for positive in positive_kws:
                    is_title = title.find(positive.strip())
                    if is_title != -1:
                        positive_item.add_value("kws_type", "positive")
                        positive_item.add_value("title", title)
                        positive_item.add_xpath("summary", ".//p[@class='cen']/a/text()")
                        positive_item.add_xpath("issuing_time", ".//div[@class='lbox']/span[2]/text()")
                        # todo
                        # positive_item.load_item("issuing_time",".//div[@class='lbox']/span[2]/text()")#爬取时间
                        detail_url = li.xpath("./div[2]/h3/a/@href").extract_first()


                        yield scrapy.Request(
                            url=urllib.parse.urljoin(response.url, detail_url),
                            callback=self.parse_detail,
                            meta={"positive_item": positive_item},
                            headers=DEFAULT_REQUEST_HEADERS
                        )

    def parse_detail(self, response):
        negative_item = response.meta.get("negative_item")
        positive_item = response.meta.get("positive_item")

        a = response.xpath("/html/body/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[3]")
        info = a[0].xpath('string(.)').extract()[0]

        if negative_item:
            negative_item.add_value("content", info)
            negative_info = negative_item.load_item()
            yield negative_info

        elif positive_item:
            positive_item.add_value("content", info)
            positive_info = positive_item.load_item()

            yield positive_info











