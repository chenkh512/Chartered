# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:56
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : ws_method.py

import suds
from suds.client import Client
from Chartered_API.common import config
from Chartered_API.common import logger

logger = logger.get_logger(__name__)


class WSRequest:

    def request(self, url, method, data):
        # 拼接URL
        self.url = config.config.get('api', 'pre_url') + url
        self.method = method
        self.data = eval(data)
        logger.info('请求URL：{0}'.format(self.url))
        logger.info('请求METHOD：{0}'.format(self.method))
        logger.info('请求DATA：{0}'.format(self.data))
        client = Client(self.url)

        try:
            resp = eval("client.service.{0}({1})".format(self.method, self.data))
            msg = resp.retInfo
        except suds.WebFault as e:
            msg = e.fault.faultstring
            print(e.document)

        logger.info("返回信息:{0}".format(msg))
        return msg
