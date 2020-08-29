# -*- coding: utf-8 -*-
import requests
import json
from config import readConfig


class Requests:
    def request(self, url, method="get", **kwargs):
        if method == "get":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "post":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "put":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "patch":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "delete":
            return requests.request(url=url, method=method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url=url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method="post", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url=url, method="put", **kwargs)

    def patch(self, url, **kwargs):
        return self.request(url=url, method="patch", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url=url, method="delete", **kwargs)


# if __name__ == "__main__":
#     obj = Requests()
#     url1 = readConfig.host+"/api/v2/fundings/get_funding_list"
#     data1 = {"type": "mine", "status": "execution"}
#     header1 = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
#         "Accept": "application/json",
#         # "Content-Type": "application/json",
#         "Cookie": readConfig.cookie
#     }
#     r = obj.request(url=url1, data=data1, headers=header1)
#     print(r.text)

