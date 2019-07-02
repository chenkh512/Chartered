# -*- coding:utf-8 -*-
# @Time     : 2019/7/1 15:18
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : test_OnlineProcess.py

#线上支付方式业务流程
import unittest,json,random,string,datetime
from ddt import ddt, data
from Chartered_API.common import contans,config,context,do_excel
from Chartered_API.common.http_method import HTTPRequest


@ddt
class OrderDeposit(unittest.TestCase):
    excel = do_excel.DoExcel(contans.case_data, '线上支付业务流程')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest()

    @data(*cases)
    def test_OrderDeposit(self, case):

        #生成时间
        createTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        beginTime = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        endTime = (datetime.datetime.now() + datetime.timedelta(hours=11)).strftime("%Y-%m-%d %H:%M:%S")
        # 创建时间
        if case.data.find('createTime') != -1:
            setattr(context.Context, 'createTime', createTime)
            case.data = case.data.replace('%createTime%', createTime)
        # 发车时间
        if case.data.find('beginTime') != -1:
            setattr(context.Context, 'beginTime', beginTime)
            case.data = case.data.replace('%beginTime%', beginTime)
        # 收车时间
        if case.data.find('endTime') != -1:
            setattr(context.Context, 'endTime', endTime)
            case.data = case.data.replace('%endTime%', endTime)

        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, json=json.loads(case.data))
        try:
            self.assertEqual(str(case.expected),str(json.dumps(resp.json())))
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()