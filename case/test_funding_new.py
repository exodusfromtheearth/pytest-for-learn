# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_funding_new.py
# Time:2020/9/6 4:31 下午

from base.method import Requests
from base.excelKeyWord import TestCaseKeyWord
from base.operationExcel import OperationExcel, ExcelVariables
import pytest
import json
from config import readConfig


excel = OperationExcel(2, 'data/Arrow', 'arrow_test.xlsx', 'fundinglist.yaml')
obj = Requests()


# caserun已经过滤不执行的测试用例
@pytest.mark.parametrize('datas', excel.caserun())
def test_funding_list(datas):
    url = readConfig.host+datas[ExcelVariables.url]
    params = datas[ExcelVariables.data]
    print(type(params))
    method = datas[ExcelVariables.method]
    content_type = datas[ExcelVariables.header]
    # print(content_type)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        'Accept': "application/json",
        # "Content-Type": content_type,
        # "Content-Type": "application/json",
        "Cookie": readConfig.cookie
    }
    expect = datas[ExcelVariables.expect]
    r = obj.request(url=url, headers=header, data=params, method=method)
    # print(r.json()["code"])
    assert expect in json.dumps(r.json(), ensure_ascii=False), "断言失败"
    # try:
    #     assert expect in json.dumps(r.json(), ensure_ascii=False)
    # except AssertionError as e:
    #     print(e)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_funding_new.py"])