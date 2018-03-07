# -*- coding: UTF-8 -*- 
from xml.dom import minidom
import xlrd #control excel
import openpyxl
import requests
import json
import time
import urllib #post
import urllib2 #get
import xiaowu
import sys
# import xmltodict #turn to xml
reload(sys)
sys.setdefaultencoding('utf-8')



book = xlrd.open_workbook(filename)
sheet = book.sheet_by_index(0) #sheet页
nrows = sheet.nrows  #get all rows

# 分别获取excel中每一个参数元素
for i in range(1,nrows):
	param1 = sheet.cell_value(i,0)
	param2 = sheet.cell_value(i,1)
	param3 = sheet.cell_value(i,2)
	p1 = param1
	p2 = param2
	p3 = param3





