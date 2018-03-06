# -*- coding: UTF-8 -*- 
from xml.dom import minidom
import xlrd
import openpyxl
import requests
import json
import time
import urllib
import urllib2
import xiaowu
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# url = 'http://dld.xikang.com/terminal/open/qqtls/getsig'
url = 'http://10.32.151.35:9091/cityapi/rest/sensordi/yuwell'
filename = r'C:\\Users\Administrator\Desktop\test\testcase_msg.xlsx'


def api_request(url,data):

	# data = urllib.urlencode(data)
	# newurl = url + '/' + data
	# response = urllib2.urlopen(newurl)
	response = urllib.urlopen(url,data)
	result = response.read()
	# msg = result("msg")
	return result

def api_data(filename):

	# book = xlrd.open_workbook(filename)
	# sheet = book.sheet_by_index(0) #sheet页
	# nrows = sheet.nrows  #get all rows

	#分别获取excel中每一个参数元素
	# for i in range(1,nrows):
	# 	param1 = sheet.cell_value(i,0)
	# 	param2 = sheet.cell_value(i,1)
	# 	param3 = sheet.cell_value(i,2)
	# 	p1 = param1
	# 	p2 = param2
	# 	p3 = param3
	# 	#对接口传参
	# 	data = xiaowu.xiaowu
	# 	ac_code = api_request(url,data)
	# 	print ac_code  #获取到接口信息
	# 	# msg = json.loads(ac_code)
	# 	# print msg["msg"]
		
	data = "<xml> <device_sn>95FF13AFB4E803F2</device_sn> <device_user>0000</device_user> <device_type>000</device_type> <device_battery>98</device_battery> <mnc>0</mnc> <lac>52c0</lac> <cid>7031</cid> <measure_data>     <sbp>120</sbp>  <dbp>80</dbp>   <pulse_rate>60</pulse_rate>     <arrhythmia>0</arrhythmia> //心率不齐，0：否， 1：是，空值：未知    <measure_time>2014-09-09 10:10:00</measure_time> </measure_data> </xml> "
	ac_code = api_request(url,data)
	print ac_code  #获取到接口信息

if __name__ == "__main__":  
	api_data(filename)

