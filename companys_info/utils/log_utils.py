# -*- coding:utf-8 -*-
import logging

# logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='log.log',
    filemode='w')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.debug("log_utils")
