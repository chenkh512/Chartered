# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:37
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : http_method.py

import requests

from Chartered_API.common.config import config
from Chartered_API.common import logger

logger = logger.get_logger(__name__)

class HTTPRequest:
    """
        公共使用一个session, cookies自动传递
       使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()  # 将method强制转成全大小

        if type(data) == str:
            data = eval(data)  # str转成字典

        # 拼接URL
        # url = config.get('api', 'pre_url') + url
        logger.debug('请求url:{0}'.format(url))
        # logger.debug('请求data:{0}'.format(data))
        logger.debug('请求json:{0}'.format(json))

        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp = None
            logger.error('UN-support method')

        logger.debug('请求response:{0}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()  # 用完记得关闭，很关键！！！

if __name__ == '__main__':
    http_request = HTTPRequest()
    params = {
        "source": "1",
        "toNumber": "2019061976298",
        "customerName": "chenkh",
        "startPlace": "重庆",
        "endPlace": "江津普通",
        "mapInfo": {
            "stationInfo": [{"lng": "106.578863", "lat": "29.517916"}, {"lng": "106.580718", "lat": "29.505948"}]},
        "phoneNumber": "15045983207",
        "beginTime": "2019-13-27 15:20:32",
        "endTime": "2019-06-28 01:20:32",
        "duration": "10",
        "numberofPassengers": "32",
        "createTime": "2019-06-27 14:20:32",
        "EnterpriseCode": "222",
        "token": ""}
    params1 = {
        "source": "1",
        "toNumber": "20190600002",
        "payType": 1,
        "amount": 500.5,
        "costType": 1,
        "name": "张三",
        "payTime": "2019-06-05 10:00:00"
    }
    resp1 = http_request.request('POST', 'http://192.9.201.103:8080/innosill/esb/ykxcharter/orders', json=params)
    resp2 = http_request.request('POST', 'http://192.9.201.103:8080/innosill/esb/charter/order/ykxEarnestMoney',json=params1)
    print(resp1.status_code)
    print(resp1.text)
    print(resp1.cookies)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)