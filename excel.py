# -*- coding: UTF-8 -*- 
from xml.dom import minidom
import xlrd
import openpyxl
import requests
import json
import sys
import HTMLParser
import os
import re
import codecs
import time
import datetime
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

url = ''
filename = ''


def api_request(url,data):

	data = urllib.parse.urlencode(data)
	newurl = urllib.request.Request(url,data)
	response1 = urllib.request.urlopen(newurl)
	result = response.read()
	response2 = result.decode('utf-8')
	code = response2.get('code')
	return code

def api_data(filename):

	book = xlrd.open_workbook(fileName)
	sheet = book.sheet_by_index(0) #sheet页
	nrows = sheet.nrows  #get all rows

	#分别获取excel中每一个参数元素
	for i in range(1,nrows):
		param1 = sheet.cell_value(i,0)
		param2 = sheet.cell_value(i,1)
		param3 = sheet.cell_value(i,2)

		p1 = param1
		p2 = param2
		p3 = param3
		#对接口传参
		data = {
		'param1' : p1,
		'param2' : p2
		}
		ac_code = api_request(url,data)

