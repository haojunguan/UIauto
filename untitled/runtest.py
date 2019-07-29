import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from function_testing_01 import model06

suite = unittest.TestSuite()

suite.addTest(model06.Month_table('test_a'))
suite.addTest(model06.Month_table('test_b'))

if __name__ == "__main__":
    fp = open('./report/' + time.strftime("%Y-%m-%d %H_%M_%S") + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='自动化用例报告',
                            description='用例执行情况'
    )
    # runner = unittest.TextTestRunner()
    runner.run(suite)