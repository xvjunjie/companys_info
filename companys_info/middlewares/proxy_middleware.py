# -*- coding:utf-8 -*-

import random
import base64

from middlewares.proxys_ip import PROXIES


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            print( proxy['user_pass'])

            encoded_user_pass = base64.encodebytes(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
