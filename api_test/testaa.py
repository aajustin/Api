#coding=utf-8 
import requests
import unittest
import json, datetime, random
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from db_fixture import myunit
import sys
import numpy as np
import pymysql
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



nowTimestyle=datetime.datetime.now().strftime("%Y-%m-%d")
nowTime=datetime.datetime.now().strftime("%Y-%m-%d");
aTime = str(nowTime)
#print(aTime)

'''



#随机选取方法
lines = f.readlines()
aa=[]  Authorization: bearer 7cb8fde5-4c51-49df-8329-041e14274a0f
for line in lines:
    temp = line.split()
    aa.append(temp[0])
aPrintNumber = random.choice(aa)
PrintNumber = aPrintNumber
print(PrintNumber)

'''
f = open("username.txt","r")
# print(f.read())
get = f.read()
aa = get.split('\n')
print(aa)
aa.reverse()
while len(aa) >0 :
	dev = aa.pop()
	break
	print(dev)
'''	
url1 = "https://app-api-stage.beautybase.cn"
s = requests.Session()
headers = {
'Content-Type':'application/json',
'Authorization':'bearer e1d0875a-6ce2-4e08-bfe0-b4fc549dce58'

}
#print(headers)

#data4 = {"deliveryType":"10","items":[{"productId":productId,"productQuantity":1}],"promotionId":"","storeId":id,"userComments":"","employeeId":"","preSelfGetTime":estimatedUseTime}
res4 = s.get(url1+"/cart/product/add?productId=8224&productQuantity=1",  headers=headers, verify=False)
print(res4.json())

data1 = {"type":"10","categoryId":"","name":"pjh测试"}
#print(headers)
res1 = s.post(url1+"/unauth/product/list?current=1&pageSize=10", json=data1, headers=headers, verify=False)
productId = res1.json()["data"]["records"][0]["id"]
print(productId)
name = res1.json()["data"]["records"][0]["name"]
#print(res1.json()["data"]["records"][0]["name"])




data2 = {"latitude":23.01626205444336,"longitude":113.28343200683594,"cityCode":"440100","provinceCode":"","cartItems":[{"productId":productId,"productQuantity":1}],"storeName":"","promotionId":""}
#print(data2)
res2 = s.post(url1+"/order/mall/listOrderMallStore", json=data2, headers=headers, verify=False)
print(res2.json()["data"])
a = res2.json()["data"]
ap = []
for i in a:
	#print(i["optional"])  optional=False 
	if i["optional"]==True:
		bb = i["id"]
		#print(bb)
		ap.append(str(bb))

	else:
		pass
        #report = open('hyk.txt', 'r')
print(ap)
aPrintNumber = random.choice(ap)
PrintNumber = aPrintNumber
print(PrintNumber)

res3 = s.get(url1+"/order/order/bespeak/list_attendant_scheduling?storeId=" + PrintNumber + "&date=" + aTime + "&attendantId=&serviceIds=129", headers=headers, verify=False)
print(res3.json()["data"]["attendants"][0]["schedulings"])
b = res3.json()["data"]["attendants"][0]["schedulings"]
for j in b:
	if j["available"]==True:
		estimatedUseTime = j["estimatedUseTime"]
		#print(estimatedUseTime)
	else:
		pass

data4 = {"deliveryType":"10","items":[{"productId":productId,"productQuantity":1}],"promotionId":"","storeId":id,"userComments":"","employeeId":"","preSelfGetTime":estimatedUseTime}
res4 = s.post(url1+"/order/mall/addOrderMall", json=data4, headers=headers, verify=False)
print(res4.json())



while len(aa) >0 :
	dev = aa.pop()
	url1 = "http://app-api-stage.beautybase.cn:WuCx4OCstReFZUUcryxR@auth-stage.beautybase.cn/oauth/token"
	payload = "grant_type=password&username=" + dev + "&grant_detailed_type=social&realm=customer&provider_id=wx3a64f83d3b7e9fff&provider_type=wechat_mini_program&scope=customer"
	headers = {
	'Content-Type':'application/x-www-form-urlencoded'
	}
	res1 = s.post(url1, data=payload, headers=headers)
	#print(res1)
	r1= res1.json()["access_token"]
	print(r1)
	#with open('D:\\YCH_YT\\username.txt','a') as f:
	#	f.write(r1 + '\n')




phone = '13560193366'
db = pymysql.connect("beautybase-dm.mysql.rds.aliyuncs.com", "dev", "Meijigongfang2018", "wface_stage", charset='utf8' )
cursor = db.cursor()
sql = "SELECT * FROM auth_account WHERE phone_number =" + "'" + phone + "'"
print(sql)
cursor.execute(sql)
results = cursor.fetchall()
#print(results)
for row in results:
	username = row[1]
	print(username)
'''

