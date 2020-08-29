import requests
from case.mybase import MyBase
import json
from common.getparam import opexcel
from common.logger1 import atp_log

class LoginCase(MyBase):
    u"""通过case_name驱动"""
    #def setUp(self):
        #warnings.simplefilter("ignore",ResourceWarning) #忽略ResourceWarning
        #self.s = requests.session()

    def test_login_success(cls):
        u"""登录成功场景"""
        atp_log.info('==========测试账号密码正确登录成功场景==========')
        test_login_success_data = opexcel.get_test_data(opexcel.get_param("LoginCase"),
                                                        "test_login_success")  # 类名与sheet页名一致,用例方法名与excel中case_name一致
        if not test_login_success_data:
            atp_log.warning("未获取到用例数据")
        url = test_login_success_data.get('url')
        atp_log.info("读取URL--【%s】"%url)
        headers = test_login_success_data.get('headers')
        data = test_login_success_data.get('data')
        atp_log.info("接口参数--【%s】"%data)
        expect_res = test_login_success_data.get('expect_res')
        res = cls.s.post(url = url,
                        headers = json.loads(headers),
                        json=json.loads(data),
                        verify = False)
        result = json.loads(res.text)["code"] #从请求返回中获取关键字
        #se1 = "SUCCESS"  #登录成功则返回SUCCESS
        atp_log.info('断言：【%s】？=【%s】'%(expect_res,result))
        cls.assertEqual(expect_res,result) #断言

    def test_login_fail(cls):
        u"""登录失败场景"""
        atp_log.info('==========测试账号密码错误登录失败场景==========')
        test_login_fail_data = opexcel.get_test_data(opexcel.get_param("LoginCase"),
                                                     "test_login_fail")  #
        if not test_login_fail_data:
            atp_log.warning("未获取到用例数据")
        url = test_login_fail_data.get('url')
        atp_log.info("读取URL--【%s】" % url)
        headers = test_login_fail_data.get('headers')
        data = test_login_fail_data.get('data')
        atp_log.info("接口参数--【%s】" % data)
        expect_res = test_login_fail_data.get('expect_res')
        res = cls.s.post(url =url,
                        headers = json.loads(headers),
                        json=json.loads(data),
                        verify = False)
        result = json.loads(res.text)["msg"]
        #se2 = "用户名或密码错误121" #账户或密码错误则返回错误data
        atp_log.info('断言：【%s】？=【%s】' % (expect_res, result))
        cls.assertEqual(expect_res,result)


if __name__ == '__main__':
    MyBase.main()