# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 16:03
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : test_Orderdeposit.py

import unittest,json,random,string,datetime
from ddt import ddt, data
from Chartered_API.common import contans,config,context,do_excel
from Chartered_API.common.http_method import HTTPRequest


@ddt
class OrderDeposit(unittest.TestCase):
    '''订单存入接口'''
    excel = do_excel.DoExcel(contans.case_data, '订单存入')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest()

    @data(*cases)
    def test_OrderDeposit(self, case):

        case.url = config.config.get('api', 'pre_url') + case.url
        # 随机生成订单，并且反射到Context类的属性中，方便后面参数调用
        random_to_number = '20190702' + ''.join(random.sample(string.digits, 3))
        if case.data.find('toNumber') != -1:
            setattr(context.Context, 'toNumber', random_to_number)
            case.data = case.data.replace('%toNumber%', random_to_number)

        # 随机生成姓名
        f_name = ['张', '金', '李', '王', '赵', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        m_name = ['大','二', '三', '四', '五', '六', '七', '八', '九' ]
        for i in range(1):
            customerName = random.choice(f_name) + random.choice(m_name)
            if case.data.find('name') != -1:
                setattr(context.Context, 'name', customerName)
                case.data = case.data.replace('%name%', customerName)

        # 随机选择起始地
        start_p = ['大学城', '沙坪坝', '机场', '菜园坝', '陈家坪', '四公里', '南广场']
        end_p = ['江津', '合川', '万州', '长寿', '铜梁', '永川', '宜宾', '北京', '上海', '万盛', '成都', '武汉', '泸州']
        for i in range(1):
            startPlace = random.choice(start_p)
            endPlace = random.choice(end_p)
            if case.data.find('startPlace') != -1:
                setattr(context.Context, 'startPlace', startPlace)
                case.data = case.data.replace('%startPlace%', startPlace)
            if case.data.find('endPlace') != -1:
                setattr(context.Context, 'endPlace', endPlace)
                case.data = case.data.replace('%endPlace%', endPlace)

        # 随机生成电话号码，并且反射到Context类的属性中，方便后面参数调用
        random_phone = '15' + ''.join(random.sample(string.digits, 6)) + '888'
        if case.data.find('phoneNumber') != -1:
            setattr(context.Context, 'phoneNumber', random_phone)
            case.data = case.data.replace('%phoneNumber%', random_phone)

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
