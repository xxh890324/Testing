import unittest
import time
from XTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录9999999-增加8-27测试备注
    test_dir = './test_case'
    suit = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                               pattern='test_*.py')

    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = './test_report/' + now_time + 'result.html'
    with (open(test_report, 'wb')) as fp:
        runner = HTMLTestRunner(stream=fp,
                                language='zh-CN',
                                title="标准化APP测试报告",
                                description="运行环境：Android 14")
        runner.run(suit)