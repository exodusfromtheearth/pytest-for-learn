# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_funding_new.py
# Time:2020/9/6 4:31 下午

from base.method import Requests
from base.operationExcel import OperationExcel, ExcelVariables
import pytest
import json
from config import readConfig


excel = OperationExcel(1, 'data/Arrow', 'arrow_test.xlsx', 'fundinglist.yaml')
obj = Requests()


@pytest.mark.parametrize('datas', excel.caserun())
def test_funding_list(datas):
    url = readConfig.host+datas[ExcelVariables.url]
    params = datas[ExcelVariables.data]
    method = datas[ExcelVariables.method]
    content_type = datas[ExcelVariables.header]
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept": "application/json",
        # "Content-Type": content_type,
        "Cookie": readConfig.cookie
    }
    expect = datas[ExcelVariables.expect]
    r = obj.request(url=url, headers=header, data=params, method=method)
    assert expect in json.dumps(r.json(), ensure_ascii=False)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_funding_new.py"])