# -*- coding:utf-8 -*-
# @Time     : 2019/6/28 15:42
# @Author   : shanyao
# @Email    : 1091671778@qq.com
# @File     : config.py

import configparser
from Chartered_API.common import contans

class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contans.global_file)  # 先加载global
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contans.online_file, encoding='utf-8')
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contans.test_file, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()
