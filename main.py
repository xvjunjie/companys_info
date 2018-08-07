# -*- coding:utf-8 -*-
import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "p2p_info"])#p2p_info
