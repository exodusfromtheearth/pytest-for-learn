import unittest
import warnings
import requests
from common.logger1 import atp_log
from common.getparam import OpExcel
from common.requestMethod import RunMethod
from common.writeResult import WriteResult

class MyBase(unittest.TestCase):
    """继承Unittest,处理warning."""

    @classmethod
    def setUpClass(cls):
        atp_log.info('=====测试开始=====')
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略ResourceWarning
        #cls.s = requests.session()  #session关联，会话保持
        #cls.data_dic = opexcel.get_test_data(opexcel.get_param()) #从excel获取的参数，用例继承该父类，可直接使用参数

        cls.writeResult = WriteResult()
        cls.cell = 1

    @classmethod
    def tearDownClass(cls):
        atp_log.info('=====测试结束=====')

