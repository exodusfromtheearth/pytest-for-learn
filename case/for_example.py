# -*- coding: utf-8 -*-
from config import readConfig
#
# """这是一个get请求的例子"""
# url = readConfig.host+"/api/events"
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#             "Cookie":readConfig.cookie
# }  # get方法其它加个user-Agent就可以了
#
# # cookie={"_session_id":"vliOMXKKjYjQf1HgUh%2FTF3bk%2FWOtI9cIqshUu31AZKsQm8uXiasvH85RshZ5IOHBiOSrG8trcMUNkgzebIN8C8P5vmyVJhQbE%2FRyRaaEEbkRB5nARALqa72EiX6uXa4bYw%2FkusjEv7PU6H%2FZgDddfB6Pd6EJkyAWnwVSJK1yQq2xXQKE0deqwpKoSEL%2F4pxJTw8IeUMHjt2MJgEtCflHZib5fYcoyqin9h0l61JrrwDBftpFdZLY1EGpdrCSSqsIuT%2BDXGR2TwFnAMOu2jcqtnsDgy93tB0VJtBh3SBQlhasP0D1kA%3D%3D--XIJcIT07eK6Tv66H--LXt%2FNOwjqhXKjg2RLBwghw%3D%3D"}
# data = {"active":True,
#         "page":1,
#         "page_size":20
#         }
# r = requests.get(url, headers=headers,data=data)
# result = json.loads(r.text)
# #r.json()会报错string indices must be integers,response（r）是个json数据，所以要json.loads(),才能把json格式转为python识别的格式
#
# data0 = result["data"]   # 获取data里面内容
# # print(data1[0] )      # 获取data里最上面有个
# get_result = data0[0]['name']  # 获取已签收状态
# print(get_result)
# #
# if u"Fdsdfff" in get_result:
#     print(u"返回正确")
# else:
#     print ("500")
#
#
# """这是一个post请求的例子"""
# url1=readConfig.host+"/api/attendees/batch_update"
# json1 = {"meeting_id":"4724","ids":[13541],"status":"1"}
# headers1 = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#             "Content-Type":"application/json;charset=UTF-8",
#             "Cookie":readConfig.cookie
# }
# data_json1=json.dumps(json1)
# r1=requests.post(url=url1,headers=headers1,json=json1)
# code=r1.status_code
# print(code)
# print(r1.text)
#
#
# """这是一个patch请求的例子
# 返回404的时候，基本都是请求的问题，检查url是否有空格和请求方式是否正确"""
# url2=readConfig.host+"/api/attendees/7902"
# json2={"status":5}
# # data_json2=json.dumps(json2)
# r2=requests.patch(url2,headers=headers1,json=json2)
# code2=r2.status_code
# print(code2)
# result2 = json.loads(r2.text)
# print(result2)
# data2= result2["data"]   # 获取data里面内容
# print(data2['statusDesc'] )      # 获取data里面的某个字段

'''上传文件'''
# url2=readConfig.host + "/api/bases/upload_logo"
# data2={"object_type":1,"object_id":13162}
# files2={"logo":('headshot-icon.png',open('D:\python_testcase\python_excel_testcase0407-2\ApiTest\common\headshot-icon.png','rb'),'image/jpeg')}
# header2={
#         "Cookie":readConfig.cookie
# }
# '''content-type参数，如果我们通过form-data的方式上传文件，
# 我们发送post请求的时候，headers这个参数中一定不能要包括这个值，，requests库会帮忙添加这个元素,加了可能会报错'''
# r3=requests.post(url2,data=data2,files=files2,headers=header2)
# print(r3.status_code)
# print(r3.json())

from base.operationYaml import OperationYaml
from base.method import Requests
import pytest
from config import readConfig


obj = Requests()
objYaml = OperationYaml()


# list循环赋值给参数
@pytest.mark.parametrize('testcase', objYaml.readyaml("test.yaml"))
def test_user(testcase):
    header1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": testcase["header"],
        "Cookie": readConfig.cookie
    }
    r = obj.request(url=testcase["url"], json=testcase["data"], method=testcase["method"], headers=header1)
    assert(testcase["expect"] in r.text)
    print(r.status_code)


if __name__ == "__main__":
    pytest.main(["-s", "for_example.py"])

