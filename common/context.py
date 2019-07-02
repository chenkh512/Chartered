# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:53
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : context.py

import random,re
from faker import Faker
from Chartered_API.common.config import config


class CheckSQL:

    def __init__(self, mysql):
        self.mysql = mysql

    def query_mvcode(self, mobile):
        db_name = mobile[9:11]
        table_name = mobile[8]
        sql = 'SELECT * FROM sms_db_{0}.t_mvcode_info_{1} WHERE Fmobile_no="{2}"'.format(db_name, table_name, mobile)
        print(sql)
        row = self.mysql.fetch_one(sql)
        if row:
            return row["Fverify_code"]
        return

    def query_uuid(self, reg_name):
        sql = 'select * from user_db.t_user_info where fuser_id = "{0}"'.format(reg_name)
        row = self.mysql.fetch_one(sql)
        if row:
            return row["Fuid"]
        return


class Context:
    title = None


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        match = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        param = match.group(1)  # 拿到参数化的KEY

        if hasattr(Context, param):
            v = getattr(Context, param)
        else:
            v = eval('get_{0}()'.format(param))
            setattr(Context, param, v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

    return data


def get_mobile():
    suffix = config.config.get('db', 'table_name') + config.config.get('db', 'db_name')
    prefix = ['158', '136', '130', '131', '132', '133', '149', '134', '150', '152', '153']
    middle = random.randint(10000, 99999)
    mobile = random.choice(prefix) + str(middle) + suffix
    return mobile


def get_ip():
    return '127.0.0.1'


def get_reg_name():
    f = Faker(locale='zh_CN')
    return f.name()


def get_cre_id():
    f = Faker(locale='zh_CN')
    return f.ssn()


if __name__ == '__main__':
    print(get_cre_id())
