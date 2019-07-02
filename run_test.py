import sys

sys.path.append('./')  # project根目录地址


import unittest
import HTMLTestRunnerNew
from Chartered_API.common import contans

discover = unittest.defaultTestLoader.discover(contans.case_dir, "test_C*.py")

with open(contans.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="包车业务接口自动化测试",
                                              description="API",
                                              tester="陈科宏")
    runner.run(discover)