# -*- coding: utf-8 -*-
# from base.operationExcel import OperationExcel


class TestCaseKeyWord:
    """
    定义测试用例关键字类
    """
    case_id = 0
    case_name = 1
    is_execute = 2
    url = 3
    method = 4
    header = 5
    data = 6
    case_depend = 7
    """case依赖"""
    case_depend_data = 8
    """依赖的返回数据"""
    field_depend = 9
    """数据依赖字段"""
    expect = 10
    actual_status_code = 11
    result = 12


# 获取用例id
#     def get_case_id(self, row):
#         return self.case_id
#
# # 获取用例名称
#     def get_case_name(self, row):
#         return self.case_name
#
# # 用例是否执行
#     def get_case_is_execute(self, row):
#         return self.is_execute
#
# # 接口url
#     def get_case_url(self, row):
#         return self.url
#
# # 用例方法
#     def get_case_method(self, row):
#         return self.method
#
# # 请求头
#     def get_case_header(self, row):
#         return self.header
#
# # 请求参数
#     def get_case_data(self, row):
#         return self.data
#
# # 预期结果
#     def get_case_expect(self, row):
#         return self.expect
#
# # 实际状态码
#     def get_case_actual_status_code(self, row):
#         return self.actual_status_code
#
# # 用例执行结果
#     def get_case_result(self, row):
#         return self.result
#
#     def get_case_depend(self, row):
#         """case依赖"""
#         return self.case_depend
#
#     def get_case_depend_data(self, row):
#         """依赖的返回数据"""
#         return self.case_depend_data
#
#     def get_case_field_depend(self, row):
#         """数据依赖字段"""
#         return self.field_depend

