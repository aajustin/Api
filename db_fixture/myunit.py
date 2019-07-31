#coding=utf-8  
import unittest
import requests
import json 
import os, sys,re
import random
import time, datetime
from demo import Webrequests


class MyTest(unittest.TestCase):
    '''接口测试'''
  
    def setUp(self):
        nowTimestyle=datetime.datetime.now().strftime("%Y-%m-%d")
        nowTime=datetime.datetime.now().strftime("%Y-%m-%d");
        self.aTime = str(nowTime)
        f = open("username.txt","r")
        # print(f.read())
        get = f.read()
        aa = get.split('\n')
        #print(aa)
        self.url = "https://app-api-stage.beautybase.cn"
        self.para = {"key":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","date":"2017-3-22"}    
        self.run=Webrequests()
        aa.reverse()
        #print(aa)
        while len(aa) >0 :
            dev = aa.pop()
            #print("==============" + dev)
            self.headers ={'Content-Type':'application/json',
            'Authorization':'bearer ' + dev} 
            print(self.headers)
            return self.headers
        #self.verify=False  requests

    def tearDown(self):
        pass

