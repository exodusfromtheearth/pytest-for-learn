# -*- coding: utf-8 -*-
import xlrd
from base.filepublic import filepath
from base.excelKeyWord import TestCaseKeyWord
from base.operationYaml import OperationYaml


class OperationExcel(OperationYaml):
    def __init__(self, num, path1, path2):
        self.excelpath = path1
        self.yamlpath = path2
        self.num = num

    def getsheet(self):
        book = xlrd.open_workbook(self.excelpath)
        return book.sheet_by_index(self.num)

# 获取用例名称
    def get_case_name(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().case_name)

# # 用例是否执行
#     def get_case_is_execute(self, row):
#         return self.getvalue(row=row, col=TestCaseKeyWord().is_execute)
#
# 请求参数；由于excel表格中的值是str类型所以需要转化一下
    def get_case_data(self, row):
        return self.getsheet().cell_value(row, TestCaseKeyWord().data)

    def get_case_json(self, row):
        return self.readyaml(self.yamlpath)[int(self.get_case_data(row))]
#
# # 实际状态码
#     def get_case_actual_status_code(self, row):
#         return self.getvalue(row=row, col=TestCaseKeyWord().actual_status_code)


if __name__ == '__main__':
    # print(filepath(fileroot='data', filename='arrow_test.xlsx'))
    # obj = OperationExcel(0, r"D:\python_testcase\python_excel_testcase0407-2\ApiTest\data\arrow_test.xlsx",r"D:\python_testcase\python_excel_testcase0407-2\ApiTest\data\fundingcase.yaml")
    obj = OperationExcel(0, filepath('data', 'arrow_test.xlsx'),filepath('data', 'fundingcase.yaml'))
    print(obj.get_case_name(1))
    print(obj.get_case_data(1))
    print(obj.get_case_json(1))
