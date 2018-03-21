import unittest

from HTMLTestRunner import HTMLTestRunner
import time

# suite = unittest.TestSuite()
# suite.addTest(test_case.test_baidu.MyTest("test_baidu"))
# suite.addTest(test_case.test_youdao.MyTest("test_youdao"))
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #
    # testunit = unittest.TestSuite()
    # testunit.addTest(baidu("test_baidu_search"))

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')

    runner.run(discover)
    fp.close()