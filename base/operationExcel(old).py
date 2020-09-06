# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from base.filepublic import filepath
from base.excelKeyWord import TestCaseKeyWord
from base.operationYaml import OperationYaml


class OperationExcel(OperationYaml):
    def __init__(self, num, root, excelname, yamlname):
        self.fileroot = root
        self.excelname = excelname
        self.yamlname = yamlname
        self.num = num
        self.book = xlrd.open_workbook(filepath(root, excelname))

    def getsheet(self):
        return self.book.sheet_by_index(self.num)

# 将接口返回值写入Excel
    def write_case_depend(self, content, row):
        rb = self.book
        wb = copy(rb)
        w_sheet = wb.get_sheet(self.num)
        w_sheet.write(row, TestCaseKeyWord.case_depend, content)
        wb.save(filepath(self.fileroot, self.excelname))

# 将接口返回的状态码写入Excel
    def write_actual_status_code(self, content, row):
        rb = self.book
        wb = copy(rb)
        w_sheet = wb.get_sheet(self.num)
        w_sheet.write(row, TestCaseKeyWord.actual_status_code, content)
        wb.save(filepath(self.fileroot, self.excelname))

# 将执行结果写入Excel，例如passed
    def write_reslut(self, content, row):
        rb = self.book
        wb = copy(rb)
        w_sheet = wb.get_sheet(self.num)
        w_sheet.write(row, TestCaseKeyWord.result, content)
        wb.save(filepath(self.fileroot, self.excelname))

    def getrows(self):
        '''获取总行数'''
        return self.getsheet().nrows

    def getcols(self):
        '''获取总列数'''
        return self.getsheet().ncols


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

#接口url包含ID
    def get_case_url_hasid(self, rd_row, wd_row):
        # row_index = 0
        # for item in range(1, self.getrows()):
        #     url = self.getsheet().cell_value(item, TestCaseKeyWord().url)
        #     case_depend = self.getsheet().cell_value(rd_row, TestCaseKeyWord.case_depend)
        #     if "{id}" in url:
        #         newurl = str(url).replace('{id}', str(int(case_depend)))
        #         return newurl
        #     else:
        #         return url
        url = self.getsheet().cell_value(wd_row, TestCaseKeyWord().url)
        case_depend = self.getsheet().cell_value(rd_row, TestCaseKeyWord.case_depend)
        if "{id}" in url:
            newurl = str(url).replace('{id}', str(int(case_depend)))
            return newurl
        else:
            return url

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
        return self.readyaml(self.fileroot, self.yamlname)[int(self.get_case_data(row))]["para"]

# 预期结果---------------------------------
    def get_case_expect(self, row):
        num = self.getsheet().cell_value(row, TestCaseKeyWord().expect)
        return self.readyaml(self.fileroot, self.yamlname)[int(num)]['expect']

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

    def getexcelvalue(self):
        value = list()
        title = self.getsheet().row_values(0)
        for row in range(1, self.getrows()):
            rowvalue = self.getsheet().row_values(row)
            value.append(dict(zip(title, rowvalue)))
        return value


if __name__ == '__main__':
    obj = OperationExcel(2, 'data/Arrow', 'arrow_test.xlsx', 'fundinglist.yaml')
    # obj.write_case_depend(920, 6)
    # print(obj.get_case_name(1))
    # print(obj.get_case_json(1))
    # print(obj.get_case_url_hasid(6, 7))


