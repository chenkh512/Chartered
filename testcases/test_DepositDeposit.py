# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 16:08
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : test_DepositDeposit.py

import unittest,json,random,string,datetime
from ddt import ddt, data
from Chartered_API.common import contans,config,context,do_excel
from Chartered_API.common.http_method import HTTPRequest

@ddt
class DepositDeposit(unittest.TestCase):
    '''定金存入接口'''
    excel = do_excel.DoExcel(contans.case_data, '定金存入')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest()

    @data(*cases)
    def test_DepositDeposit(self, case):

        case.url = config.config.get('api', 'pre_url') + case.url

        #随机生成订单号
        random_to_number = '20190701' + ''.join(random.sample(string.digits, 3))
        if case.data.find('toNumber') != -1:
            setattr(context.Context, 'toNumber', random_to_number)
            case.data = case.data.replace('%toNumber%', random_to_number)

        #生成当前时间
        payTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if case.data.find('payTime') != -1:
            setattr(context.Context, 'payTime', payTime)
            case.data = case.data.replace('%payTime%', payTime)

        # 随机生成姓名
        f_name = ['张', '金', '李', '王', '赵', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        m_name = ['大','二', '三', '四', '五', '六', '七', '八', '九' ]
        for i in range(1):
            customerName = random.choice(f_name) + random.choice(m_name)
            if case.data.find('name') != -1:
                setattr(context.Context, 'name', customerName)
                case.data = case.data.replace('%name%', customerName)

        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url,data=None, json=json.loads(case.data))
        try:
            self.assertEqual(case.expected,str(json.dumps(resp.json())))
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()