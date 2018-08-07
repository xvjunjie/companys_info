# -*- coding: utf-8 -*-

# Scrapy settings for companys_info project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import sys
import os

BOT_NAME = 'companys_info'

SPIDER_MODULES = ['companys_info.spiders']
NEWSPIDER_MODULE = 'companys_info.spiders'

# LOG_LEVEL = "WARNING"

project_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(project_dir)
sys.path.insert(0, os.path.join(base_dir, "companys"))

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
COOKIES_ENABLED =False
# cookie
# COOKIES = {
#     '_ga': 'GA1.2.1976295663.1532532228',
#     '_gid': 'GA1.2.519700921.1532707543',
#     'ssuid': '1727575405',
#     'RTYCID': 'c0ba604db3c34b749421e83c4dc26f71',
#     'csrfToken': 'L44Ncz9us8erhTMYZdXq2yFp',
#     'token': 'c11902c5f9994da6b1e44265cde68cdc',
#     '_utm': '41a4aca066174366b0bdc8e2faac2937',
#     'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1532617253,1532707541,1532756111,1532861903',
#     'tyc-user-info': '%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTMwMTY3NTAwOCIsImlhdCI6MTUzMjg2MTk5MCwiZXhwIjoxNTQ4NDEzOTkwfQ.yAzh1R0627_5_OE513VCGiWY_2ZI0JkZ_vnHM2WAxNlO3F5zI2sv7W7nsYjNflq2wQtFWB5L2xnZVxB079IaUQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522347%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522onum%2522%253A%25221%2522%252C%2522mobile%2522%253A%252215301675008%2522%257D',
#     'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTMwMTY3NTAwOCIsImlhdCI6MTUzMjg2MTk5MCwiZXhwIjoxNTQ4NDEzOTkwfQ.yAzh1R0627_5_OE513VCGiWY_2ZI0JkZ_vnHM2WAxNlO3F5zI2sv7W7nsYjNflq2wQtFWB5L2xnZVxB079IaUQ',
#     'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1532861994',
# }

# 请求头信息
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'www.tianyancha.com',
    'Referer': 'https://www.tianyancha.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.tianyancha.com',
    'DNT': '1',
    'Referer': 'https://www.tianyancha.com/search?key=%E5%B9%BF%E4%B8%9C%E7%B2%A4%E4%BE%A8%E5%9B%BD%E9%99%85%E6%97%85%E8%A1%8C%E7%A4%BE%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'companys_info.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     # 'middlewares.proxy_middleware.ProxyMiddleware': 1,
#     'middlewares.useragent_middleware.RotateUserAgentMiddleware': 2,
#
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'pipelines.CompanysPipeline': 1,
    # 'pipelines.InsertInfoPipeline': 2,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONGODB_SERVER = 'mongodb://localhost:27017'
MONGODB_DB = 'companys_info'
MONGODB_COLLECTION = 'business_info'
