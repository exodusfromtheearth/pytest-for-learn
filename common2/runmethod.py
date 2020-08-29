# -*- coding: utf-8 -*-
import requests
import json
from config import readConfig

class Requests:
    def request(self,url,method="get",**kwargs):
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "multipart/form-data",
            "Cookie": readConfig.cookie
        }
        if method=="get":
            return self.get(url=url,headers=header,**kwargs)
        elif method=="post":
            return self.post(url=url,headers=header,**kwargs)
        elif method=="put":
            return self.put(url=url,headers=header,**kwargs)
        elif method=="patch":
            return self.patch(url=url,headers=header,**kwargs)
        elif method=="delete":
            return self.delete(url=url,headers=header,**kwargs)

    def get(self,url,**kwargs):
        return requests.get(url=url,headers=header,data=data)

    def post(self,url,**kwargs):
        return requests.post(url=url,headers=header,data=data)

    def put(self,url,**kwargs):
        return requests.put(url=url,headers=header,data=data)

    def patch(self,url,**kwargs):
        return requests.patch(url=url,headers=header,data=data)

    def delete(self, url,**kwargs):
        return requests.delete(url=url,headers=header,data=data)

