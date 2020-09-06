# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_funding.py
# Time:2020/9/5 2:04 下午

from base.operationExcel import OperationExcel
import pytest
import json
from base.method import Requests
from config import readConfig


class TestFunding:
    excelobj = OperationExcel(2, 'data/Arrow', 'arrow_test.xlsx', 'fundinglist.yaml')
    obj = Requests()

    def test_funding_001(self):
        '''获取项目列表'''
        url = readConfig.host+self.excelobj.get_case_url(1)
        data1 = self.excelobj.get_case_json(1)
        # print(self.excelobj.get_case_json(1))
        # data1 = {'type': 'all', 'status': 'source'}
        method = self.excelobj.get_case_method(1)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(1),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data1, method=method)
        assert self.excelobj.get_case_expect(1) in json.dumps(r.json(), ensure_ascii=False)
        status_code = r.json()['code']
        self.excelobj.write_actual_status_code(status_code, 1)


    def test_funding_002(self):
        '''获取项目列表'''
        url = readConfig.host+self.excelobj.get_case_url(2)
        data = self.excelobj.get_case_json(2)
        method = self.excelobj.get_case_method(2)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        assert self.excelobj.get_case_expect(2) in json.dumps(r.json(), ensure_ascii=False)

    def test_funding_003(self):
        '''获取项目列表'''
        url = readConfig.host + self.excelobj.get_case_url(3)
        data = self.excelobj.get_case_json(3)
        method = self.excelobj.get_case_method(3)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        assert self.excelobj.get_case_expect(3) in json.dumps(r.json(), ensure_ascii=False)

    def test_funding_004(self):
        '''获取项目列表'''
        url = readConfig.host + self.excelobj.get_case_url(4)
        data = self.excelobj.get_case_json(4)
        method = self.excelobj.get_case_method(4)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        assert self.excelobj.get_case_expect(4) in json.dumps(r.json(), ensure_ascii=False)

    def test_funding_005(self):
        '''获取项目列表'''
        url = readConfig.host + self.excelobj.get_case_url(5)
        data = self.excelobj.get_case_json(5)
        method = self.excelobj.get_case_method(5)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        assert self.excelobj.get_case_expect(5) in json.dumps(r.json(), ensure_ascii=False)

    def test_funding_006(self):
        '''新建项目'''
        url = readConfig.host + self.excelobj.get_case_url(6)
        data = self.excelobj.get_case_json(6)
        method = self.excelobj.get_case_method(6)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        # print(self.excelobj.get_case_expect(6))
        # print(r.json()['data']['statusDesc'])
        # assert self.excelobj.get_case_expect(6) in json.dumps(r.json(), ensure_ascii=False)
        assert self.excelobj.get_case_expect(6) == r.json()['data']['statusDesc']
        funding_id = r.json()["data"]["id"]
        self.excelobj.write_case_depend(funding_id, 6)
        status_code = r.json()['code']
        self.excelobj.write_actual_status_code(status_code, 6)

    def test_funding_007(self):
        '''查看项目'''
        url = readConfig.host + self.excelobj.get_case_url_hasid(6, 7)
        data = self.excelobj.get_case_json(7)
        method = self.excelobj.get_case_method(7)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        assert self.excelobj.get_case_expect(7) == r.json()['data']['statusDesc']
        status_code = r.json()['code']
        self.excelobj.write_actual_status_code(status_code, 7)

    def test_funding_008(self):
        '''编辑项目'''
        url = readConfig.host + self.excelobj.get_case_url_hasid(6, 8)
        data = self.excelobj.get_case_json(8)
        method = self.excelobj.get_case_method(8)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            # "Content-Type": self.excelobj.get_case_header(2),
            "Cookie": readConfig.cookie
        }
        r = self.obj.request(url=url, headers=header, data=data, method=method)
        # assert self.excelobj.get_case_expect(8) in json.dumps(r.json(), ensure_ascii=False)
        # assert self.excelobj.get_case_expect(8) in r.json()
        status_code = r.json()['code']
        self.excelobj.write_actual_status_code(status_code, 8)


if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_funding.py"])

