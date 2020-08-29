# -*- coding: utf-8 -*-
#读取多条测试用例
#1、导入requests模块
import requests
#从 class_12_19.do_excel1导入read_data函数
from common2.do_excel2 import read_data
from common2.do_excel2 import write_data
from common2.do_excel2 import count_case
#定义http请求函数

COOKIE = None
def http_request2(method,url,data):

 if method=='get':
  print('发起一个get请求')
  result=requests.get(url, data, cookies=COOKIE)
 else:
  print('发起一个post请求')
  result=requests.post(url,data,cookies=COOKIE)
 return result #返回响应体
 # return result.json() #返回响应结果：结果是字典类型：{'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}


#从Excel读取到多条测试数据
sheets=['login', 'recharge', 'withdraw']
for sheet1 in sheets:
 max_row=count_case(sheet1)
 print(max_row)
 for case_id in range(1,max_row):
  data=read_data(sheet1,case_id)
  print('读取到第{}条测试用例:'.format(data[0]))
  print('测试数据 ',data)
  #print(type(data[2]))
  #调用函数发起http请求
  result=http_request2(data[4],data[2],eval(data[3]))
  print('响应结果为 ',result.json())
  if result.cookies:
    COOKIE=result.cookies

   #将测试实际结果写入excel
   #write_data(case_id+1,6,result['code'])
  write_data(sheet1,case_id+1,7,str(result.json()))
  #对比测试结果和期望结果
  if result.json()['code']==str(data[5]):
   print('测试通过')
   #将用例执行结果写入Excel
   write_data(sheet1,case_id+1,8,'Pass')
  else:
   write_data(sheet1,case_id+1,8,'Fail')
   print('测试失败')

