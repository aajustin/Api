#coding:utf-8
import requests
import json

class Webrequests:
    def get(self,url,para,headers):
        try:
            r = requests.get(url,params=para,headers=headers)
            #print("获取返回的状态码",r.status_code)
            json_r = r.json()
            #print("json类型转化成python数据类型",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
    def post(self,url,para,headers):
        try:
            r = requests.post(url,data=para,headers=headers)
            #print("获取返回的状态码",r.status_code)
            json_r = r.json()
            #print("json类型转化成python数据类型",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = requests.post(url,data=data,headers=headers)
            #print("获取返回的状态码",r.status_code)
            json_r = r.json()
            #print("json类型转化成python数据类型",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
            
if __name__ == '__main__':
    pass
    #url = "https://app-api-stage.beautybase.cn/cart/product/add?productId=8224&productQuantity=1"
    #para = {"key":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","date":"2017-3-22"}
    #headers ={'Content-Type':'application/json',
    #'Authorization':'bearer e1d0875a-6ce2-4e08-bfe0-b4fc549dce58'}

    #q = Webrequests()

    #q.get(url,para,headers)
    #q.post(url,para,headers)
    #q.post_json(url,para,headers)