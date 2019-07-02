# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:38
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : contans.py

import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
print(base_dir)

root_dir = os.path.dirname(base_dir)

case_data = os.path.join(base_dir, 'data', 'chartered_case.xlsx')
print(case_data)

global_file = os.path.join(base_dir, 'config', 'global.conf')
print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
print(test_file)

log_dir = os.path.join(base_dir, 'log')
print(log_dir)

case_dir = os.path.join(base_dir, 'testcases')
print(case_dir)

report_dir = os.path.join(base_dir, 'reports')
print(report_dir)