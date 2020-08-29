# -*- coding: utf-8 -*-
from base.operationExcel import OperationExcel
from base.method import Requests
import pytest
from config import readConfig
from base.filepublic import filepath


class Testfunding:

    def test_com_001(self):
        excel = OperationExcel(0, filepath('data', 'arrow_test.xlsx'), filepath('data', 'fundingcase.yaml'))
        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                    "Cookie": readConfig.cookie
        }
        url = readConfig.host + excel.get_case_url(1)
        r = Requests().get(url=url, headers=headers)
        print(r.content.decode('utf-8'))

    def test_com_002(self):
        excel = OperationExcel(1, filepath('data', 'arrow_test.xlsx'), filepath('data', 'fundingcase.yaml'))
        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                    "Cookie": readConfig.cookie
        }
        url = readConfig.host + excel.get_case_url(1)
        r = Requests().get(url=url, headers=headers)
        print(r.content.decode('utf-8'))

if __name__ == "__main__":
    pytest.main(["-s", "test01.py"])

# excel1 = OperationExcel(0, filepath('data', 'arrow_test.xlsx'), filepath('data', 'fundingcase.yaml'))
# obj = Requests()
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#             "Cookie": readConfig.cookie
# }
# url = readConfig.host + excel1.get_case_url(1)
# r = obj.get(url=url, headers=headers)
# result = r.text
# print(result.encode)
# print(r.content.decode('utf-8'))
