#coding:utf-8
import unittest
import json
from demo import Webrequests
import os, sys, random
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import myunit
import re

class TestMethod(myunit.MyTest):

	def test_01(self):
		url = self.url+"/cart/product/add?productId=8224&productQuantity=1"
		self.res1 = self.run.get(url,self.para,self.headers)
		#print(self.res1)

	def test_02(self):
		url = self.url+"/unauth/product/list?current=1&pageSize=10"
		data = {"type":"10","categoryId":"","name":"pjh测试"}
		bbb = self.headers
		#print(bbb)
		self.res2 = self.run.post_json(url,data,self.headers)
		#print(self.res2)
		self.productId = self.res2["data"]["records"][0]["id"]
		#print(self.productId)
		return self.productId

	def test_03(self):
		#import re
		self.productId = TestMethod.test_02(self)
		#print(self.productId)
		url = self.url+"/order/mall/listOrderMallStore"
		data = {"latitude":23.01626205444336,"longitude":113.28343200683594,"cityCode":"440100","provinceCode":"","cartItems":[{"productId":self.productId,"productQuantity":1}],"storeName":"","promotionId":""}
		self.res3 = self.run.post_json(url,data,self.headers)
		self.a = self.res3["data"]
		#print(self.a)
		self.ap = []
		for i in self.a:
			#self.ap = []
			#print(i["optional"])  optional=False 
			if i["optional"]==True:
				self.idd = i["id"]
				self.ap.append(self.idd)
				#print(self.ap)
			else:
				pass
		#print(self.ap)
		self.app = random.choice(self.ap)
		self.storeId = self.app
		#print(self.storeId)
		return self.storeId

	def test_04(self):
		self.storeId = TestMethod.test_03(self)
		#print(self.storeId)
		url = self.url+"/order/order/bespeak/list_attendant_scheduling?storeId=" + str(self.storeId) + "&date=" + self.aTime + "&attendantId=&serviceIds=129"
		#print(url)
		self.res4 = self.run.get(url,self.para,self.headers)
		self.b = self.res4["data"]["attendants"][0]["schedulings"]
		#print(self.b)
		self.ap1 = []
		for j in self.b:
			if j["available"]==True:
				self.estimatedUseTime = j["estimatedUseTime"]
				self.ap1.append(str(self.estimatedUseTime))
			else:
				pass
				#print("找不到排版记录")
		self.app1 = random.choice(self.ap1)
		self.UseTime = self.app1
		#print(self.UseTime)
		return self.UseTime

	def test_05(self):
		self.UseTime = TestMethod.test_04(self)
		self.productId = TestMethod.test_02(self)
		self.storeId = TestMethod.test_03(self)
		url = self.url+"/order/mall/addOrderMall"
		#print(url)
		data = {"deliveryType":"10","items":[{"productId":self.productId,"productQuantity":1}],"promotionId":"","storeId":str(self.storeId),"userComments":"","employeeId":"","preSelfGetTime":self.UseTime}
		#print(data)
		self.res5 = self.run.post_json(url,data,self.headers)
		#print(self.res5)
		
if __name__ == '__main__':
	unittest.main(verbosity=3)

	# 构造测试集
	#suite = unittest.TestSuite()
	# 往测试套件里面添加测试用例 （测试套件 = 测试集合）
	#suite.addTest(TestMethod("test_02"))
	#suite.addTest(TestMethod("test_05"))

	# 执行测试测试套件
	#runner = unittest.TextTestRunner()
	#runner.run(suite) 