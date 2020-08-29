# -*- coding: utf-8 -*-
import xlrd
from base.filepublic import filepath
from base.excelKeyWord import TestCaseKeyWord
from base.operationYaml import OperationYaml


class OperationExcel(OperationYaml):
    def __init__(self, num, root, excelname, yamlname):
        self.fileroot = root
        self.excelname = excelname
        self.yamlname = yamlname
        self.num = num

    def getsheet(self):
        book = xlrd.open_workbook(filepath(self.fileroot, self.excelname))
        return book.sheet_by_index(self.num)

# 获取用例名称
    def get_case_name(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().case_name)

# 获取用例id
    def get_case_id(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().case_id)

# 用例是否执行
    def get_case_is_execute(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().is_execute)

# 接口url
    def get_case_url(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().url)

# 用例方法
    def get_case_method(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().method)

# 请求头
    def get_case_header(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().header)

# 请求参数；由于excel表格中的值是str类型所以需要转化一下
    def get_case_data(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().data)

    def get_case_json(self, row):
        return self.readyaml(filepath(self.fileroot, self.yamlname))[int(self.get_case_data(row))]

# 预期结果这样处理也是可以的啊---------------------------------
    def get_case_expect(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().expect)

# 实际状态码
    def get_case_actual_status_code(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().actual_status_code)

# 用例执行结果
    def get_case_result(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().result)

    def get_case_depend(self, row):
        """case依赖"""
        return self.getsheet().cell_value(row, TestCaseKeyWord().case_depend)

    def get_case_depend_data(self, row):
        """依赖的返回数据"""
        return self.getsheet().cell_value(row, TestCaseKeyWord().case_depend_data)

    def get_case_field_depend(self, row):
        """数据依赖字段"""
        return self.getsheet().cell_value(row, TestCaseKeyWord().field_depend)


if __name__ == '__main__':
    obj = OperationExcel(0, 'data/Arrow', 'arrow_test.xlsx', 'fundingcase.yaml')
    print(obj.get_case_name(1))
    print(obj.get_case_data(1))
    print(obj.get_case_json(1))

