# -*- coding: utf-8 -*-
import yaml
from base.filepublic import filepath


class OperationYaml:
    def readyaml(self, root, name):
        with open(filepath(fileroot=root, filename=name), "r", encoding='utf-8')as f:
            return list(yaml.safe_load_all(f))

# obj = OperationYaml()
# f = obj.readyaml('data', 'test.yaml')
# print(f[0])
# print(f[2])

# for item in f:
#     print(item)


# with open(filepath(filename="test.yaml"), "r", encoding="utf-8") as f:
#     context = yaml.load(f, Loader=yaml.FullLoader)
# print("读取内容\n", context, type(context))

# test_data2 = [
#     {'url': 'http://test7.huaxing.com/api/v2/fundings/get_funding_list', 'method': 'get', 'data': {'type': 'mine', 'status': 'execution'}},
#     {'url': 'http://test7.huaxing.com/api/v2/fundings/get_funding_list2', 'method': 'get', 'data': {'type': 'all', 'status': 'execution'}}
# ]
# f = open(filepath(filename="fundingcase.yaml"), "r", encoding='utf-8')
# txt = list(yaml.safe_load_all(f))
# print(txt[0])
# print(txt[1])
# print(txt[2])
#
# for item in txt:
#     print(item)
#     print(item["url"])
# f.close()
