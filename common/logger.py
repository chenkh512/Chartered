# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:38
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : logger.py

import logging
from Chartered_API.common import contans



def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()  # 控制台
    # 把日志级别放到配置文件里面配置--优化
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contans.log_dir + '/case.log')
    # 把日志级别放到配置文件里面配置
    file_handler.setLevel('DEBUG')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
