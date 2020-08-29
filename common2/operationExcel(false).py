# -*- coding: utf-8 -*-
import os
import xlrd
from xlutils.copy import copy

# 获取当前文件的绝对路径
curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# 获取项目根目录
rootPath = os.path.abspath(os.path.dirname(curPath))
# print(rootPath)

# 获取文件路径
def filepath(fileDir="data",fileName="swagger.xls"):
    return os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),fileDir,fileName
    )
# file_path = r'data\swagger.xls'
# file_path = os.path.join(rootPath, file_path)
# print(file_path)
# 打开excel文件
data = xlrd.open_workbook(filepath())
# 获取第一张工作表（通过索引的方式）
table = data.sheets()[0]
# data_list用来存放数据
data_list = []
# 将table中第一行的数据读取并添加到data_list中
data_list.extend(table.row_values(0))
# 打印出第一行的全部数据
for item in data_list:
    print(item)

# 写入数据
copy_data = copy(data)
# 读取复制的excel的sheet页
copy_data_to_sheet = copy_data.get_sheet(0)
# 通过get_sheet()获取的sheet有write()方法，写入数据
copy_data_to_sheet.write(5, 5, "这是我写入的测试数据：哈哈")
# 保存数据
copy_data.save(file_path)