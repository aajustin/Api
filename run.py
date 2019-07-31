from HTMLTestRunner import HTMLTestRunner
import unittest
import time


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=' kinhom_pc auto test report',
                            description='info：windows 7 ,browser：chrome')
    discover = unittest.defaultTestLoader.discover('./api_test', pattern='test_api.py')
    runner.run(discover)
    fp.close()
