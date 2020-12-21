# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from base.filepublic import filepath
from base.excelKeyWord import TestCaseKeyWord
from base.operationYaml import OperationYaml


class ExcelVariables:
    case_id = "caseID"
    case_name = "描述"
    is_execute = "是否执行"
    url = "请求地址"
    method = "请求方式"
    header = "请求头"
    data = "请求参数"
    case_depend = "请求依赖"    # case 依赖
    case_depend_data = "依赖返回的数据"
    field_depend = "数据依赖字段"
    expect = "期望结果"
    actual_status_code = "返回状态码"
    result = "实际结果"

class OperationExcel(OperationYaml):
    def __init__(self, num, root, excelname, yamlname):
        self.fileroot = root
        self.excelname = excelname
        self.yamlname = yamlname
        self.num = num
        self.book = xlrd.open_workbook(filepath(root, excelname))

    def getsheet(self):
        '''获取excel文件的第几张表格'''
        return self.book.sheet_by_index(self.num)

    def getrows(self):
        '''获取总行数'''
        return self.getsheet().nrows

    def getcols(self):
        '''获取总列数'''
        return self.getsheet().ncols

    def getexceldatas(self):
        '''第一步获取所有测试用例'''
        runlist = list()
        title = self.getsheet().row_values(0)
        for row in range(1, self.getrows()):
            rowvalue = self.getsheet().row_values(row)
            runlist.append(dict(zip(title, rowvalue)))
        return runlist

    def caserunwithoutpara(self):
        '''第二步获取可执行的测试用例'''
        runlist = list()
        for row in self.getexceldatas():
            isrun = row[ExcelVariables.is_execute]
            if isrun == 'yes':
                runlist.append(row)
            else:
                pass
        return runlist

    def caserun(self):
        '''第三步关联yaml文件，获取测试用例的参数data和期望结果expect'''
        runlist = list()
        for item in self.caserunwithoutpara():
            num = item[ExcelVariables.expect]
            item[ExcelVariables.data] = self.readyaml(self.fileroot, self.yamlname)[int(num)]["para"]
            item[ExcelVariables.expect] = self.readyaml(self.fileroot, self.yamlname)[int(num)]["expect"]
            runlist.append(item)
        return runlist

    # 将返回的状态码和断言结果写入Excel
    def write_actual_return(self, content1, content2, row):
        rb = self.book
        wb = copy(rb)
        w_sheet = wb.get_sheet(self.num)
        w_sheet.write(row, TestCaseKeyWord.actual_status_code, content1)
        w_sheet.write(row, TestCaseKeyWord.result, content2)
        wb.save(filepath(self.fileroot, self.excelname))


if __name__ == '__main__':
    obj = OperationExcel(2, 'data/Arrow', 'arrow_test3.xlsx', 'fundinglist.yaml')
    # for item in obj.getexceldatas():
    #     print(item[ExcelVariables.is_execute])
    # print(obj.getsheet().cell_value(1, 12))
    # for i in range(0, obj.getcols()):
    #     print(obj.getsheet().cell_value(1, i))
    # print(obj.caserunwithoutpara())
    # for i in obj.caserun():
    #     print(i["请求参数"],i["期望结果"])
    # print(obj.caserun())
    # obj.write_case_depend("断言成功", 1)
    obj.write_actual_return("200", "断言成功", 1)
